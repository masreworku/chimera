"""Small runner that demonstrates how a Worker would request a post.

This script shows the intended flow: Worker -> Judge -> MCP(Twitter).
Judge must approve before the MCP is called.
"""

import asyncio
import typing as t

from src.mcp.twitter import TwitterMCP


class Judge:
    """Stub Judge that approves all non-sensitive posts.

    Real Judge should validate against persona tone, relevance, and safety rules.
    """

    async def validate_post(self, text: str) -> dict:
        # Simple heuristic: reject if it contains the word 'sensitive'
        if "sensitive" in text.lower():
            return {"verdict": "rejected", "score": 0.0}
        return {"verdict": "approved", "score": 1.0}


async def main(text: str):
    judge = Judge()
    decision = await judge.validate_post(text)
    if decision["verdict"] != "approved":
        print("Judge rejected the post:", decision)
        return

    twitter = TwitterMCP()
    try:
        resp = await twitter.post_tweet(text)
    except NotImplementedError:
        print("Twitter MCP not implemented yet. This is a placeholder.")
        return

    print("Post response:", resp)


if __name__ == "__main__":
    example_text = "Hello Chimera followers!"
    asyncio.run(main(example_text))
