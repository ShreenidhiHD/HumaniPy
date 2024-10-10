import unittest
from unittest.mock import patch, MagicMock
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from humani_py.movements import random_mouse_move

class TestRandomMouseMove(unittest.TestCase):
    @patch('humani_py.movements.ActionChains')
    @patch('humani_py.movements.time.sleep')
    @patch('humani_py.movements.random.uniform')
    @patch('humani_py.movements.random.randint')
    @patch('humani_py.movements.random.random')
    def test_random_mouse_move(self, mock_random, mock_randint, mock_uniform, mock_sleep, mock_action_chains):
        # Mock WebDriver and WebElement
        mock_driver = MagicMock(spec=WebDriver)
        mock_element = MagicMock(spec=WebElement)

        # Set up mock return values
        mock_element.location = {'x': 100, 'y': 100}
        mock_driver.execute_script.side_effect = [
            [500, 500],  # Initial mouse position
            None,  # For each scrollBy call
        ]
        mock_uniform.return_value = 0.1
        mock_randint.return_value = 50
        mock_random.return_value = 0.5

        # Create a mock ActionChains object
        mock_action_chain = mock_action_chains.return_value

        # Call the function being tested
        random_mouse_move(mock_driver, mock_element, test_mode=True)

        # Assertions
        self.assertTrue(mock_driver.execute_script.called)
        self.assertEqual(mock_driver.execute_script.call_count, 102)  # 1 for initial position + 100 steps + 1 for overshoot correction
        mock_action_chains.assert_called_once_with(mock_driver)
        mock_action_chain.move_to_element.assert_called_once_with(mock_element)
        mock_action_chain.perform.assert_called_once()
        self.assertTrue(mock_sleep.called)
        self.assertTrue(mock_uniform.called)
