from unittest.mock import MagicMock
from humani_py.stealth import apply_stealth

def test_apply_stealth():
    mock_driver = MagicMock()

    apply_stealth(mock_driver, test_mode=True)

    mock_driver.execute_cdp_cmd.assert_called_with(
        'Network.setUserAgentOverride',
        {'userAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    )