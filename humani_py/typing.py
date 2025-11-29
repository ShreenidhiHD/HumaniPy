import random
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

def human_typing(element: WebElement, text: str, min_speed: float = 0.05, max_speed: float = 0.2, typo_chance: float = 0.05) -> None:
    """
    Simulates human-like typing by adding a random delay between keystrokes and occasional typos.
    
    Parameters:
    - element: The target WebElement.
    - text: The text to type.
    - min_speed: Minimum delay between keystrokes.
    - max_speed: Maximum delay between keystrokes.
    - typo_chance: Probability (0.0 to 1.0) of making a typo per character.
    """
    qwerty_neighbors = {
        'a': 'qsxz', 'b': 'vghn', 'c': 'xdfv', 'd': 'erfc', 'e': 'wsdfr',
        'f': 'rtgv', 'g': 'tyhb', 'h': 'yujn', 'i': 'ujko', 'j': 'uikm',
        'k': 'iolm', 'l': 'opk', 'm': 'njk', 'n': 'bhjm', 'o': 'iklp',
        'p': 'ol', 'q': 'wa', 'r': 'edft', 's': 'wadz', 't': 'rfgy',
        'u': 'yhji', 'v': 'cfgb', 'w': 'qase', 'x': 'zsdc', 'y': 'tghu',
        'z': 'asx'
    }

    for char in text:
        # Simulate typo
        if random.random() < typo_chance:
            neighbor = random.choice(qwerty_neighbors.get(char.lower(), char))
            if neighbor != char:
                element.send_keys(neighbor)
                time.sleep(random.uniform(min_speed, max_speed))
                # Backspace
                element.send_keys(Keys.BACKSPACE)
                time.sleep(random.uniform(min_speed, max_speed) * 0.5)
        
        element.send_keys(char)
        
        # Variable delay
        delay = random.uniform(min_speed, max_speed)
        # Add extra delay for spaces or punctuation
        if char in ' .,?!':
            delay += 0.1
            
        time.sleep(delay)
