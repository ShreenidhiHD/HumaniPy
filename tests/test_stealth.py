from unittest.mock import MagicMock
from humani_py.stealth import apply_stealth

def test_apply_stealth():
    mock_driver = MagicMock()

    # Adjust the mock return value to match the actual behavior
    mock_driver.execute_cdp_cmd.return_value = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"

    apply_stealth(mock_driver)

    # Verify that the correct user agent was set
    mock_driver.execute_cdp_cmd.assert_called_with(
        'Network.setUserAgentOverride',
        {'userAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    )
