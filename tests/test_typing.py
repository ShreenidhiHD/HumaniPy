from humani_py.typing import human_typing
from unittest.mock import MagicMock

def test_human_typing():
    mock_element = MagicMock()
    text = "Hello"
    human_typing(mock_element, text)
    
    assert mock_element.send_keys.call_count == len(text)
