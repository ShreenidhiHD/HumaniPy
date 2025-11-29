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

def test_random_mouse_move(mock_dependencies):
    mock_action_chains, mock_sleep, mock_uniform, mock_randint, mock_random = mock_dependencies
    
    # Create mock objects
    mock_driver = MagicMock(spec=WebDriver)
    mock_element = MagicMock(spec=WebElement)
    mock_body = MagicMock(spec=WebElement)
    
    # Setup element rect
    mock_element.rect = {'x': 100, 'y': 100, 'width': 50, 'height': 50}
    
    # Setup driver calls
    mock_driver.execute_script.side_effect = [
        1920, # viewport width
        1080  # viewport height
    ]
    mock_driver.find_element.return_value = mock_body
    
    # Setup random values
    mock_randint.side_effect = [
        0,    # start_x
        0,    # start_y
        20    # steps (if not test_mode, but we use test_mode=True first)
    ]
    
    # Mock ActionChains
    mock_action_chain = MagicMock()
    mock_action_chains.return_value = mock_action_chain
    
    # Configure chaining
    mock_action_chain.move_to_element.return_value = mock_action_chain
    mock_action_chain.move_to_element_with_offset.return_value = mock_action_chain
    
    # Test in test mode
    random_mouse_move(mock_driver, mock_element, test_mode=True)
    
    # Assertions
    # Should get viewport size
    assert mock_driver.execute_script.call_count == 2
    # Should find body
    mock_driver.find_element.assert_called_with("tag name", "body")
    # Should create ActionChains
    mock_action_chains.assert_called_with(mock_driver)
    
    # Should move to start
    mock_action_chain.move_to_element_with_offset.assert_any_call(mock_body, 0, 0)
    
    # Should move in steps (20 steps in test mode)
    # We won't check every single call, but ensure perform is called
    assert mock_action_chain.perform.call_count >= 20
    
    # Should move to final element
    mock_action_chain.move_to_element.assert_called_with(mock_element)