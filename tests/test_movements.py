from unittest.mock import MagicMock, patch
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from humani_py.movements import random_mouse_move

@patch('humani_py.movements.ActionChains')
def test_random_mouse_move(mock_action_chains):
    mock_driver = MagicMock()
    mock_element = MagicMock(spec=WebElement)

    # Create a mock ActionChains object
    mock_action_chain = mock_action_chains.return_value

    # Call the function being tested
    random_mouse_move(mock_driver, mock_element, test_mode=True)

    # Verify that move_to_element_with_offset was called once with correct arguments
    mock_action_chain.move_to_element_with_offset.assert_called_once_with(mock_element, 0, 0)
    # Verify that perform was called once
    mock_action_chain.perform.assert_called_once()
