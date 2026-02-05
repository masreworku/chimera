# Project Chimera: Functional Specification (functional.md)
## 1. Persona & Narrative Agency
The system must maintain the "soul" of each digital influencer across all platforms.

Storytelling Engine: The agent shall generate long-form backstories and daily "life events" based on its SOUL.md definition.

Voice Consistency: All generated text must pass a "Tone Check" against the persona’s defined linguistic markers (e.g., "Gen-Z Tech Optimist" vs. "Cynical Macro Trader").

## 2. Perception & Trend Analysis
Agents do not post in a vacuum; they must react to the "vibe" of the internet.

Trend Ingestion: The agent must fetch top-ranking keywords from specified niches (e.g., AI, Crypto, Fashion) via the Twitter/X MCP server.

Relevance Filtering: Ingested data is scored. Only content with a Relevance Threshold > 0.75 (relative to the persona's interests) will trigger a "Reaction Task."

Memory Retrieval: Before responding, agents must query Weaviate to see if they have commented on this topic before to avoid repetitive behavior.

## 3. Content Creation Workflows
The system uses the Planner-Worker-Judge loop to ensure high-quality output.

User Story: As an Agent, I need to decompose a high-level goal (e.g., "Announce my new ETH validator") into a multi-step task graph including copy drafting, image generation, and scheduling.

Multimodal Execution:

Text: Drafting posts, threads, and replies.

Visual: Generating consistent character art using LoRAs or reference IDs.

Quality Gates: No content is published unless the Judge Agent returns an approved status.

## 4. Agentic Commerce (Economic Agency)
Agents are authorized to participate in the on-chain economy.

Self-Funding: Agents can check their Coinbase AgentKit wallet balance to determine if they have enough gas/funds for a proposed action.

Transaction Logic: Agents may execute swaps or transfers if the "CFO Judge" validates the transaction against the agent's monthly budget.

## 5. Human-in-the-Loop (HITL) & Safety
Escalation Protocol: If a "Judge" identifies a "Sensitive Topic" (Politics, Legal, or High-Value Transaction), the task is moved to a human_review queue.

The "Kill Switch": A global orchestrator command must be able to pause all agent activities across the network instantly.