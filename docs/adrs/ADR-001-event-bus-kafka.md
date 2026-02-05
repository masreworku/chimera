# ADR-001 — Event Bus: Kafka

Date: 2026-02-05
Owner: TBD

## Context
Project Chimera must support a very high throughput of agent events (task scheduling, status, audit logs) across many ephemeral workers. The system needs a durable, ordered, horizontally scalable messaging substrate with good ecosystem support for stream processing and replay.

## Decision
Select Apache Kafka as the primary event bus for inter-agent messaging and event streaming.

## Rationale
- Kafka provides high throughput, horizontal scalability, and durable retention with partitioning and replication.
- Strong ecosystem for stream processing (Kafka Streams, ksqlDB) and connector support for sinks/sources.
- Ability to replay streams for debugging, recovery, and offline analysis.

## Alternatives Considered
- RabbitMQ: simpler broker semantics but weaker throughput and replay semantics.
- Pulsar: comparable feature set; operational familiarity and ecosystem maturity favored Kafka for initial rollout.

## Consequences
- Operational complexity: requires running and operating a Kafka cluster (or managed Kafka service).
- Cost: storage and broker resources for retention windows will incur cost; tune retention and compaction policies.
- Integration: adapt workers and planners to publish/subscribe via Kafka clients or connectors.

## Notes
- Consider managed Kafka (Confluent Cloud, MSK) for faster operational onboarding.
- Define retention/compaction policy per topic (task queue vs audit log).
