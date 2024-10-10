from unittest.mock import MagicMock
from humani_py.scrolling import scroll_page

def test_scroll_page():
    mock_driver = MagicMock()

    # Mock the scroll height value
    mock_driver.execute_script.return_value = 1000  # Assuming page height is 1000

    scroll_page(mock_driver, direction="down", percentage=50, speed=1.5)

    # Adjust assertion to match the float value
    mock_driver.execute_script.assert_called_with('window.scrollBy(0, 500.0);')
