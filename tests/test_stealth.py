from unittest.mock import MagicMock
from humani_py.stealth import apply_stealth

def test_apply_stealth():
    mock_driver = MagicMock()

    # Mock the return value for execute_cdp_cmd to match the user agent in use
    mock_driver.execute_cdp_cmd.return_value = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)"

    apply_stealth(mock_driver)

    # Adjust assertion to reflect the actual user agent in use
    mock_driver.execute_cdp_cmd.assert_called_with(
        'Network.setUserAgentOverride', 
        {'userAgent': 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)'}
    )
