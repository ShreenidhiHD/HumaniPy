from unittest.mock import MagicMock, patch
from humani_py.scrolling import scroll_page

@patch('humani_py.scrolling.time.sleep')
@patch('humani_py.scrolling.random.randint')
def test_scroll_page(mock_randint, mock_sleep):
    mock_driver = MagicMock()

    # Mock return values for: scrollHeight, innerHeight, pageYOffset
    # We use a side_effect function to handle infinite calls if needed, 
    # but simpler is to just provide enough values or use return_value for the loop.
    # The loop calls execute_script to scroll.
    
    def side_effect(script):
        if "scrollHeight" in script:
            return 2000
        if "innerHeight" in script:
            return 1000
        if "pageYOffset" in script:
            return 0
        return None # For scrollTo calls

    mock_driver.execute_script.side_effect = side_effect
    
    # Mock random chunk size to be predictable
    mock_randint.return_value = 100

    scroll_page(mock_driver, direction="down", percentage=50, speed=1.5)

    # Target scroll is 50% of (2000 - 1000) = 500
    # Current is 0. Target is 500.
    # Chunk is 100. So it should take 5 steps: 100, 200, 300, 400, 500.
    
    # Verify that scrollTo was called
    assert mock_driver.execute_script.call_count >= 3 
    
    # Check if the final scroll reached the target
    mock_driver.execute_script.assert_any_call("window.scrollTo({top: 500, behavior: 'smooth'});")
