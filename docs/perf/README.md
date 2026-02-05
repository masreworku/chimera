Benchmarking guidance — Project Chimera

Purpose
- Provide a lightweight, reproducible way to benchmark task throughput and worker concurrency for the Redis-backed task queue used in the FastRender Swarm PoC.

Goals
- Validate that the architecture can meet the throughput targets in `research/architecture_strategy.md` (Dev/Staging/Prod).
- Provide a simple load generator and worker harness to measure tasks/sec, task latency, and failure behavior.

What is included
- `tools/bench/benchmark_redis_queue.py` — async Python script to run producers and worker pools against a Redis list queue and report produced/consumed rates.
- `tools/bench/requirements.txt` — minimal Python dependencies.

Quick start
1. Install Python 3.10+ and create a venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r tools/bench/requirements.txt
```

2. Start Redis locally (default `redis://localhost:6379`). Example using Docker:

```powershell
docker run --rm -p 6379:6379 redis:7
```

3. Run a short benchmark (10s, 4 producers, 8 workers):

```powershell
python tools/bench/benchmark_redis_queue.py --duration 10 --producers 4 --workers 8
```

Interpreting results
- "Produced" vs "Consumed" counts: should be equal at steady state.
- Tasks/sec: consumed / elapsed_seconds.
- Average processing latency: measured if producers attach a timestamp to each message.

Next steps
- Extend to benchmark Kafka event bus and end-to-end Planner→Worker→Judge flows.
- Add k6 or Locust profiles for HTTP-facing components (Orchestrator Dashboard APIs).
