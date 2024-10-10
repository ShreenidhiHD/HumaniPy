from selenium.webdriver.remote.webelement import WebElement
from unittest.mock import MagicMock
from humani_py.movements import random_mouse_move

def test_random_mouse_move():
    mock_driver = MagicMock()
    mock_element = MagicMock(spec=WebElement)  # Mock WebElement
    
    random_mouse_move(mock_driver, mock_element)
    
    # Add an assert statement to verify that the move_to_element_with_offset was called
    mock_driver.ActionChains().move_to_element_with_offset.assert_called()
