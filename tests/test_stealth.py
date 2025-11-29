from unittest.mock import MagicMock, call
from humani_py.stealth import apply_stealth

def test_apply_stealth():
    mock_driver = MagicMock()

    apply_stealth(mock_driver, test_mode=True)

    # Verify User Agent override
    mock_driver.execute_cdp_cmd.assert_any_call(
        'Network.setUserAgentOverride',
        {'userAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
    )
    
    # Verify WebDriver property hiding
    # We check if the command was called, exact source match might be fragile if whitespace changes,
    # but we can check the command name at least.
    calls = mock_driver.execute_cdp_cmd.call_args_list
    assert any(c[0][0] == 'Page.addScriptToEvaluateOnNewDocument' for c in calls)