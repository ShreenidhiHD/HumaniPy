from unittest.mock import MagicMock
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from humani_py.movements import random_mouse_move

def test_random_mouse_move():
    mock_driver = MagicMock()
    mock_element = MagicMock(spec=WebElement)  # Mock WebElement

    # Mock ActionChains and its methods
    mock_action_chain = MagicMock(spec=ActionChains)
    mock_driver.ActionChains.return_value = mock_action_chain

    # Call the function being tested
    random_mouse_move(mock_driver, mock_element)

    # Verify that move_to_element_with_offset was called
    mock_action_chain.move_to_element_with_offset.assert_called_with(mock_element, 0, 0)  
