# ADR-002 — Semantic Memory: Weaviate

Date: 2026-02-05
Owner: TBD

## Context
Agents require long-term, searchable persona memory for retrieval-augmented generation (RAG). The store must support vector similarity search, metadata filters, and efficient indexing for embeddings produced by chosen models.

## Decision
Choose Weaviate as the semantic memory (vector database) for persona recall and RAG workflows.

## Rationale
- Weaviate offers a native vector search engine with flexible schema and metadata filtering.
- Active community and integrations for embeddings and similarity search.
- Support for hybrid queries (vector + filters) simplifies persona recall logic.

## Alternatives Considered
- Pinecone: managed service with strong performance; considered for reduced operational overhead.
- Milvus: high-performance vector DB; heavier ops footprint.

## Consequences
- Operational considerations: run Weaviate in a managed or self-hosted mode; plan for vector index sizing and cost.
- Model compatibility: ensure embedding model output is compatible with chosen index configuration.

## Notes
- Evaluate managed Weaviate offerings or self-host with autoscaling depending on expected vector count.
