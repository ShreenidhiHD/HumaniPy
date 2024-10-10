from humani_py.movements import random_mouse_move
from unittest.mock import MagicMock

def test_random_mouse_move():
    mock_driver = MagicMock()
    mock_element = MagicMock()
    random_mouse_move(mock_driver, mock_element)

    # Check if action chain move_to_element_with_offset was called
    mock_driver.ActionChains().move_to_element_with_offset.assert_called()
