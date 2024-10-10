from unittest.mock import patch, MagicMock
from selenium.webdriver.remote.webelement import WebElement
from humani_py.movements import random_mouse_move

@patch('humani_py.movements.ActionChains')
@patch('humani_py.movements.random.uniform')
@patch('humani_py.movements.time.sleep')
@patch('humani_py.movements.webdriver.WebDriver.execute_script')
def test_random_mouse_move(mock_execute_script, mock_sleep, mock_uniform, mock_action_chains):
    mock_driver = MagicMock()
    mock_element = MagicMock(spec=WebElement)

    # Set mock return values for uniform and execute_script
    mock_uniform.side_effect = [0, 0.5, 0.1]  # Mock overshoot and speed values
    mock_execute_script.side_effect = [[500, 500]]  # Mock current mouse position
    
    # Create a mock ActionChains object
    mock_action_chain = mock_action_chains.return_value

    # Call the function being tested
    random_mouse_move(mock_driver, mock_element, overshoot=True, easing=True, random_pauses=True, test_mode=True)

    # Verify that ActionChains was instantiated with the driver
    mock_action_chains.assert_called_once_with(mock_driver)

    # Verify that move_to_element was called once
    mock_action_chain.move_to_element.assert_called_once_with(mock_element)

    # Verify that perform was called
    mock_action_chain.perform.assert_called()

    # Check that execute_script was called for getting mouse position
    mock_execute_script.assert_called()

    # Check that random.uniform was used for random pauses and overshoot
    mock_uniform.assert_any_call(0.1, 0.5)

    # Verify that sleep was called for pauses
    mock_sleep.assert_called()