from unittest.mock import MagicMock
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from humani_py.movements import random_mouse_move

def test_random_mouse_move():
    mock_driver = MagicMock()
    mock_element = MagicMock(spec=WebElement)

    mock_action_chain = MagicMock(spec=ActionChains)
    mock_driver.ActionChains.return_value = mock_action_chain

    random_mouse_move(mock_driver, mock_element, test_mode=True)

    mock_action_chain.move_to_element_with_offset.assert_called_once_with(mock_element, 0, 0)
    mock_action_chain.perform.assert_called_once()