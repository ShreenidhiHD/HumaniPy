from humani_py.stealth import apply_stealth
from unittest.mock import MagicMock

def test_apply_stealth():
    mock_driver = MagicMock()
    apply_stealth(mock_driver)
    
    # Assert that the user agent override was set
    mock_driver.execute_cdp_cmd.assert_called_with('Network.setUserAgentOverride', {'userAgent': mock_driver.execute_cdp_cmd()})
