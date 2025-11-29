from humani_py.typing import human_typing
from unittest.mock import MagicMock, patch

def test_human_typing():
    mock_element = MagicMock()
    text = "Hello"
    
    with patch('humani_py.typing.random.random') as mock_random:
        mock_random.return_value = 0.9
        human_typing(mock_element, text)
        assert mock_element.send_keys.call_count == len(text)

def test_human_typing_with_typos():
    mock_element = MagicMock()
    text = "A"
    
    with patch('humani_py.typing.random.random') as mock_random, \
         patch('humani_py.typing.random.choice') as mock_choice:
        
        # We need to provide enough return values for the loop.
        # Logic for 1 char "A" with typo:
        # 1. random() < typo_chance (1.0) -> True. (Value: 0.0)
        # 2. choice() -> 'B'.
        # 3. random() for delay -> 0.5
        # 4. random() for backspace delay -> 0.5
        # 5. random() for normal char delay -> 0.5
        
        # So we need at least 4 floats.
        mock_random.side_effect = [0.0, 0.5, 0.5, 0.5, 0.5, 0.5] 
        mock_choice.return_value = 'B'
        
        human_typing(mock_element, text, typo_chance=1.0)
        
        # Should be: Typo char + Backspace + Correct char = 3 calls
        assert mock_element.send_keys.call_count >= 3
