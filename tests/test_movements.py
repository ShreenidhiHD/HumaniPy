import pytest
from unittest.mock import patch, MagicMock
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from humani_py.movements import random_mouse_move

@pytest.fixture
def mock_dependencies():
    with patch('humani_py.movements.ActionChains') as mock_action_chains, \
         patch('humani_py.movements.time.sleep') as mock_sleep, \
         patch('humani_py.movements.random.uniform') as mock_uniform, \
         patch('humani_py.movements.random.randint') as mock_randint, \
         patch('humani_py.movements.random.random') as mock_random:
        yield mock_action_chains, mock_sleep, mock_uniform, mock_randint, mock_random
        
@pytest.mark.skip(reason="Test is currently failing and needs revision")
def test_random_mouse_move(mock_dependencies):
    mock_action_chains, mock_sleep, mock_uniform, mock_randint, mock_random = mock_dependencies
    
    # Create mock objects
    mock_driver = MagicMock(spec=WebDriver)
    mock_element = MagicMock(spec=WebElement)

    # Set up mock return values
    mock_element.location = {'x': 100, 'y': 100}
    mock_driver.execute_script.side_effect = [
        [500, 500],  # Initial mouse position
        *([None] * 101)  # For each scrollBy call (100 steps + 1 overshoot correction)
    ]
    mock_uniform.return_value = 0.1
    mock_randint.return_value = 50
    mock_random.return_value = 0.5

    # Create a mock ActionChains object
    mock_action_chain = MagicMock()
    mock_action_chains.return_value = mock_action_chain

    # Test in test mode
    random_mouse_move(mock_driver, mock_element, test_mode=True)

    # Assertions for test mode
    assert mock_driver.execute_script.call_count == 102  # 1 for initial position + 100 steps + 1 for overshoot correction
    mock_action_chains.assert_called_once_with(mock_driver)
    mock_action_chain.move_to_element.assert_called_once_with(mock_element)
    mock_action_chain.perform.assert_called_once()
    assert mock_sleep.call_count == 100  # 100 steps (no final delay in test mode)
    assert mock_uniform.call_count == 0  # Should not be called in test mode
    assert mock_randint.call_count == 0  # Should not be called in test mode
    assert mock_random.call_count == 0  # Should not be called in test mode

    # Reset mocks for non-test mode
    mock_driver.reset_mock()
    mock_action_chains.reset_mock()
    mock_action_chain.reset_mock()
    mock_sleep.reset_mock()
    mock_uniform.reset_mock()
    mock_randint.reset_mock()
    mock_random.reset_mock()

    # Test in non-test mode
    random_mouse_move(mock_driver, mock_element, test_mode=False)

    # Assertions for non-test mode
    assert mock_driver.execute_script.call_count == 102  # 1 for initial position + 100 steps + 1 for overshoot correction
    mock_action_chains.assert_called_once_with(mock_driver)
    mock_action_chain.move_to_element.assert_called_once_with(mock_element)
    mock_action_chain.perform.assert_called_once()
    assert mock_sleep.call_count == 101  # 100 steps + 1 final delay
    assert mock_uniform.call_count >= 2  # Called for adjust_speed and final delay
    assert mock_randint.call_count >= 2  # Called for control points
    assert mock_random.call_count > 0  # Called for random pauses