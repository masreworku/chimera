from __future__ import annotations

import typing as t


class TwitterMCP:
    """MCP wrapper for posting to Twitter/X.

    Usage contract:
    - `post_tweet(text, media_paths=None, in_reply_to=None) -> dict`
    - Returns a dict with at least `status` and `tweet_id` keys on success.

    This is a stub implementation intentionally left unimplemented so the
    initial test can fail (TDD flow). Implementations must be async and
    should handle auth, retries, rate limits, and error mapping.
    """

    async def post_tweet(
        self,
        text: str,
        media_paths: t.Optional[t.List[str]] = None,
        in_reply_to: t.Optional[str] = None,
    ) -> dict:
        """Post a tweet. Raise NotImplementedError until implemented.

        Args:
            text: The tweet text (<= 280 chars recommended).
            media_paths: Optional list of local file paths to upload.
            in_reply_to: Optional tweet id to reply to.

        Returns:
            A dict containing at least `status` and `tweet_id` on success.
        """
        raise NotImplementedError("TwitterMCP.post_tweet is not implemented yet")
