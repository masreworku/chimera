# Project Chimera: Technical Specification (technical.md)
## 1. System Architecture Overview
The system follows the FastRender Swarm Architecture, utilizing a decoupled approach where the Planner (Strategic), Worker (Execution), and Judge (Governance) operate as independent nodes.

## 2. Data Persistence (Database Schema)
The system uses a dual-database approach to handle both structured transactions and unstructured "memory."

### 2.1 Relational Schema (PostgreSQL)
Table: agents: id (UUID), name, wallet_address, persona_id (FK), status.

Table: tasks: id (UUID), agent_id (FK), type (Content/Research/OnChain), status, payload (JSONB), result (JSONB).

Table: ledger: id (UUID), agent_id (FK), transaction_hash, amount, currency, purpose.

### 2.2 Vector Schema (Weaviate)
Class: EpisodicMemory: Stores short-term interactions for context window retrieval.

Class: SemanticKnowledge: Stores long-term domain knowledge and brand guidelines.

Properties: content (text), embedding (vector), timestamp, source_url.

## 3. API Contracts (JSON Interface)
All inter-agent communication must adhere to the following schemas to ensure consistency across the swarm.

### 3.1 Task Assignment Schema
JSON
{
  "task_id": "uuid-v4",
  "priority": "high|medium|low",
  "actor": "worker_agent",
  "action": "generate_content",
  "parameters": {
    "platform": "twitter",
    "topic_ids": ["eth_gaming", "base_l2"],
    "persona_voice": "vibe_coding_expert"
  }
}
### 3.2 Judge Validation Schema
JSON
{
  "validation_id": "uuid-v4",
  "target_task_id": "uuid-v4",
  "score": 0.0, // 0.0 to 1.0
  "verdict": "approved|rejected|revision_required",
  "feedback": "string",
  "governance_flag": false
}
## 4. Agentic Commerce (Coinbase AgentKit)
Wallet Provider: CDK (Coinbase Developer Kit).

Network: Base Mainnet / Sepolia Testnet.

Capabilities: transfer, trade, check_balance.

Guardrails: The "CFO Judge" must intercept any transaction request exceeding the pre-defined daily_gas_limit or spend_limit.

## 5. Infrastructure & CI/CD
Containerization: Dockerized microservices for each agent role.

Monitoring: MCP Telemetry via Tenx MCP Sense for real-time "thinking" logs.

Deployment: GitHub Actions workflow for automated testing (TDD) before deployment.