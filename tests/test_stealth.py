from unittest.mock import MagicMock
from humani_py.stealth import apply_stealth

def test_apply_stealth():
    mock_driver = MagicMock()
    
    # Mock the return value for execute_cdp_cmd
    mock_driver.execute_cdp_cmd.return_value = "mocked_user_agent"
    
    apply_stealth(mock_driver)
    
    # Assert that the user agent override was set
    mock_driver.execute_cdp_cmd.assert_called_with('Network.setUserAgentOverride', {'userAgent': 'mocked_user_agent'})
