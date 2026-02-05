import pytest

from src.mcp.twitter import TwitterMCP


@pytest.mark.asyncio
async def test_post_tweet_returns_ok():
    """Failing test: expects a successful post response structure.

    This test is intentionally written to fail until the MCP is implemented.
    """
    mcp = TwitterMCP()
    resp = await mcp.post_tweet("Hello from Chimera test")
    assert isinstance(resp, dict)
    assert resp.get("status") == "ok"
    assert "tweet_id" in resp
