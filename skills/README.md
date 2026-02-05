# Chimera Agent Skills (Runtime)

This directory defines the atomic capabilities of the Project Chimera Influencer Swarm. Each skill follows a strict Input/Output JSON contract.

## 1. skill_trend_analyzer
**Purpose:** Scans social media for high-velocity keywords.
- **Input:** {"niche": "string", "limit": int}
- **Output:** {"trends": [{"tag": "string", "velocity_score": float}]}

## 2. skill_content_generator
**Purpose:** Generates multimodal content (text/image) based on a persona.
- **Input:** {"prompt_base": "string", "platform": "twitter|farcaster", "include_image": bool}
- **Output:** {"text_content": "string", "image_asset_path": "string", "character_id": "uuid"}

## 3. skill_wallet_manager (via Coinbase AgentKit)
**Purpose:** Executes on-chain financial operations.
- **Input:** {"action": "transfer|swap|balance", "amount": float, "asset": "USDC|ETH"}
- **Output:** {"status": "success|fail", "tx_hash": "string", "remaining_balance": float}

## 4. Execution Guardrails
All skills must be invoked through the **Worker** class and validated by the **Judge** class before the result is finalized.