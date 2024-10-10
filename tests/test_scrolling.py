from humani_py.scrolling import scroll_page
from unittest.mock import MagicMock

def test_scroll_page():
    mock_driver = MagicMock()
    scroll_page(mock_driver, direction="down", percentage=50, speed=1.5)

    # Assert that scroll was called with the correct JavaScript
    mock_driver.execute_script.assert_called_with('window.scrollBy(0, -0.5);')
