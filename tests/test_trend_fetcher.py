import pytest
from typing import Dict, List

# This represents the API Contract defined in specs/technical.md
REQUIRED_TREND_FIELDS = ["tag", "velocity_score", "source"]

def test_trend_data_structure_contract():
    """
    Test 3.1.1: Asserts that trend data matches the technical.md API contract.
    This test will fail until the trend_fetcher service is implemented.
    """
    # In a real scenario, this would call your actual fetcher service
    # For now, we simulate what the service *should* return
    from skills.trend_analyzer import fetch_trends # This import will likely fail now
    
    sample_trends = fetch_trends(niche="ai_agents", limit=5)
    
    assert isinstance(sample_trends, list), "Trends must be returned as a list"
    assert len(sample_trends) > 0, "Trend list should not be empty"
    
    for trend in sample_trends:
        for field in REQUIRED_TREND_FIELDS:
            assert field in trend, f"Missing required field '{field}' in trend object"
        assert isinstance(trend["velocity_score"], float), "velocity_score must be a float"