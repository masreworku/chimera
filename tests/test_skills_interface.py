import pytest
from pydantic import ValidationError

def test_skill_content_generator_input_validation():
    """
    Test 3.1.2: Asserts that skill_content_generator rejects invalid payloads.
    Ensures the 'Governor' logic is working as per functional.md.
    """
    # This test expects a Skill class that uses Pydantic for validation
    from skills.content_generator import ContentGeneratorSkill
    
    # Test valid input
    valid_payload = {
        "prompt_base": "Future of AI in Ethiopia",
        "platform": "twitter",
        "include_image": True
    }
    skill = ContentGeneratorSkill(**valid_payload)
    assert skill.platform == "twitter"

    # Test invalid input (should raise error)
    invalid_payload = {
        "prompt_base": 12345, # Should be a string
        "platform": "invalid_platform" 
    }
    with pytest.raises(ValidationError):
        ContentGeneratorSkill(**invalid_payload)

def test_skill_wallet_manager_budget_guardrail():
    """
    Test 3.1.3: Asserts the 'CFO Judge' logic prevents overspending.
    """
    from skills.wallet_manager import WalletManager
    
    manager = WalletManager(daily_limit=50.0)
    
    # This should fail if the skill doesn't check the budget (as per technical.md)
    with pytest.raises(PermissionError, match="BudgetExceeded"):
        manager.execute_transaction(amount_usdc=100.0, asset="USDC")