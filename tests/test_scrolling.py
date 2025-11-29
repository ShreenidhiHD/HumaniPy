from unittest.mock import MagicMock, patch
from humani_py.scrolling import scroll_page

@patch('humani_py.scrolling.time.sleep')
@patch('humani_py.scrolling.random.randint')
def test_scroll_page(mock_randint, mock_sleep):
    mock_driver = MagicMock()

    # Mock return values for: scrollHeight, innerHeight, pageYOffset
    mock_driver.execute_script.side_effect = [
        2000, # scrollHeight
        1000, # innerHeight
        0     # pageYOffset
    ]
    
    # Mock random chunk size to be predictable
    mock_randint.return_value = 100

    scroll_page(mock_driver, direction="down", percentage=50, speed=1.5)

    # Target scroll is 50% of (2000 - 1000) = 500
    # Current is 0. Target is 500.
    # Chunk is 100. So it should take 5 steps: 100, 200, 300, 400, 500.
    
    # Verify that scrollTo was called
    assert mock_driver.execute_script.call_count >= 3 # At least the initial 3 gets + scroll calls
    
    # Check if the final scroll reached the target
    # The last call should be scrollTo 500
    mock_driver.execute_script.assert_any_call("window.scrollTo({top: 500, behavior: 'smooth'});")
