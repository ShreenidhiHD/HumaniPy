import random
import time
from selenium.webdriver.remote.webelement import WebElement

def human_typing(element: WebElement, text: str, min_speed: float = 0.1, max_speed: float = 0.3) -> None:
    """Simulates human-like typing by adding a random delay between keystrokes."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_speed, max_speed))
