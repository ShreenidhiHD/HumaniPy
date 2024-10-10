from unittest.mock import patch, MagicMock
from selenium.webdriver.remote.webelement import WebElement
from humani_py.movements import random_mouse_move

@patch('selenium.webdriver.ActionChains')
@patch('selenium.webdriver.remote.webdriver.WebDriver.execute_script')
@patch('humani_py.movements.time.sleep')
@patch('humani_py.movements.random.uniform')
def test_random_mouse_move(mock_uniform, mock_sleep, mock_execute_script, mock_action_chains):
    mock_driver = MagicMock()
    mock_element = MagicMock(spec=WebElement)

    # Mock return values
    mock_uniform.side_effect = [0, 0.5, 0.1]
    mock_execute_script.return_value = [500, 500]  # Mock the current mouse position

    # Create a mock ActionChains object
    mock_action_chain = mock_action_chains.return_value

    # Call the function being tested
    random_mouse_move(mock_driver, mock_element, test_mode=True)

    # Verify that ActionChains was instantiated with the driver
    mock_action_chains.assert_called_once_with(mock_driver)

    # Verify that move_to_element was called once
    mock_action_chain.move_to_element.assert_called_once_with(mock_element)

    # Verify that perform was called
    mock_action_chain.perform.assert_called()

    # Check that execute_script was called for getting mouse position
    mock_execute_script.assert_called()

    # Check that random.uniform was used for overshoot and pauses
    mock_uniform.assert_any_call(0.1, 0.5)

    # Verify that sleep was called for pauses
    mock_sleep.assert_called()
