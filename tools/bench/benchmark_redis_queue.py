#!/usr/bin/env python3
"""Async Redis queue benchmark harness.

Simulates producers that LPUSH messages into a Redis list and workers that BRPOP them.
Reports produced/consumed counts and approximate throughput.
"""

import argparse
import asyncio
import json
import random
import string
import time
from typing import Dict

import redis.asyncio as aioredis


def make_payload(size: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))


async def producer(name: str, redis_url: str, queue: str, payload_size: int, stop_event: asyncio.Event, produced_counter: Dict[str, int]):
    r = aioredis.from_url(redis_url)
    while not stop_event.is_set():
        msg = {
            "id": f"{name}-{time.time_ns()}",
            "ts": time.time(),
            "payload": make_payload(payload_size),
        }
        await r.lpush(queue, json.dumps(msg))
        produced_counter["count"] += 1
    await r.close()


async def worker(name: str, redis_url: str, queue: str, stop_event: asyncio.Event, consumed_counter: Dict[str, int]):
    r = aioredis.from_url(redis_url)
    while not stop_event.is_set():
        try:
            item = await r.brpop(queue, timeout=1)
        except Exception:
            item = None
        if item:
            # item = (queue, payload)
            _queue, payload = item
            try:
                data = json.loads(payload)
            except Exception:
                data = None
            # simulate small processing time (non-LLM step)
            await asyncio.sleep(0.005)
            consumed_counter["count"] += 1
    await r.close()


async def run_benchmark(args):
    stop_event = asyncio.Event()
    produced_counter = {"count": 0}
    consumed_counter = {"count": 0}

    producers = [producer(f"P{i}", args.redis, args.queue, args.payload_size, stop_event, produced_counter) for i in range(args.producers)]
    workers = [worker(f"W{i}", args.redis, args.queue, stop_event, consumed_counter) for i in range(args.workers)]

    tasks = [asyncio.create_task(coro) for coro in producers + workers]

    start = time.time()
    try:
        await asyncio.sleep(args.duration)
    except asyncio.CancelledError:
        pass
    stop_event.set()
    await asyncio.gather(*tasks, return_exceptions=True)
    end = time.time()

    elapsed = end - start
    produced = produced_counter["count"]
    consumed = consumed_counter["count"]

    print(f"Elapsed: {elapsed:.2f}s")
    print(f"Produced: {produced}")
    print(f"Consumed: {consumed}")
    print(f"Throughput (consumed/sec): {consumed/elapsed:.2f}")


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--duration", type=int, default=30, help="Duration in seconds")
    p.add_argument("--producers", type=int, default=2)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--queue", type=str, default="chimera:task_queue")
    p.add_argument("--payload-size", type=int, default=256)
    p.add_argument("--redis", type=str, default="redis://localhost:6379")
    return p.parse_args()


def main():
    args = parse_args()
    try:
        asyncio.run(run_benchmark(args))
    except KeyboardInterrupt:
        print("Interrupted")


if __name__ == "__main__":
    main()
