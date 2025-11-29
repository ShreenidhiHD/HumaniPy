# HumaniPy

"Because even your bots deserve to act a little more human."

HumaniPy is a Python package that helps simulate human-like behavior in web automation tasks. It adds random delays, human-like interactions, and other features to make web scraping and automation safer and more natural.

## Features:

- **True Mouse Movements**: Simulates realistic mouse cursor paths using Bezier curves and `ActionChains`.
- **Enhanced Stealth**: Hides `navigator.webdriver` and randomizes window dimensions to avoid fingerprinting.
- **Natural Typing**: Simulates human typing with variable speeds and occasional typos (with corrections).
- **Smooth Scrolling**: Scrolls the page naturally with smooth behavior and random pauses.
- **Retries**: Automatically retry actions if they fail.

## Installation:

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage:

### Basic Example:
```python
from selenium import webdriver
from humani_py.stealth import apply_stealth
from humani_py.typing import human_typing
from humani_py.scrolling import scroll_page
from humani_py.movements import random_mouse_move

driver = webdriver.Chrome()

# Apply stealth mode
apply_stealth(driver)

# Navigate to a website
driver.get('https://example.com')

# Simulate typing in a search box
search_box = driver.find_element("name", "q")
human_typing(search_box, "Hello World")

# Move mouse to an element naturally
random_mouse_move(driver, search_box)

# Scroll naturally down the page
scroll_page(driver, direction="down", percentage=80, speed=2.0)
```

### Validation:
```python
from humani_py.utils import validate_percentage, validate_speed

# Validate scroll percentage
validate_percentage(80)

# Validate typing speed
validate_speed(1.5)
```