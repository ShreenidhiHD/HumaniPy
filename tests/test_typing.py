from humani_py.typing import human_typing
from unittest.mock import MagicMock, patch

def test_human_typing():
    mock_element = MagicMock()
    text = "Hello"
    
    # We can either mock random to avoid typos, or assert >= len(text)
    # Let's mock random to ensure deterministic behavior for this basic test
    with patch('humani_py.typing.random.random') as mock_random:
        # Return 0.9 to avoid typos (typo_chance is usually low, e.g. 0.05)
        # If typo_chance is 0.05, random() < 0.05 triggers typo.
        # So returning 0.9 ensures no typo.
        mock_random.return_value = 0.9
        
        human_typing(mock_element, text)
        
        # Without typos, call count should be exactly len(text)
        assert mock_element.send_keys.call_count == len(text)

def test_human_typing_with_typos():
    mock_element = MagicMock()
    text = "A"
    
    with patch('humani_py.typing.random.random') as mock_random, \
         patch('humani_py.typing.random.choice') as mock_choice:
        
        # Force a typo on the first char
        # 1. random() < typo_chance (0.05) -> True (return 0.0)
        # 2. random.choice -> returns 'B' (neighbor)
        # 3. random() for delay -> return 0.5
        # 4. random() for backspace delay -> return 0.5
        # 5. random() for normal char delay -> return 0.5
        
        # We need to control the sequence of random() calls carefully or just assert > len(text)
        # Simpler approach: Assert that with typos enabled, we get more calls.
        
        human_typing(mock_element, text, typo_chance=1.0) # Force typos
        
        # Should be: Typo char + Backspace + Correct char = 3 calls
        assert mock_element.send_keys.call_count >= 3
