# HumaniPy 🐍✨

_"Because even your bots deserve to act a little more human."_

HumaniPy is a Python package that helps simulate human-like behavior in web automation tasks. It adds random delays, human-like scrolling, stealth, and more to make automation safer and more natural.

## Features:
- **Random Delays**: Mimic human hesitations with random pauses.
- **Stealth Mode**: Change headers, user-agent, and more to avoid detection.
- **Scrolling**: Scroll naturally, just like a human.
- **Typing Simulation**: Type like a real person with random keystrokes.
- **Mouse Movements**: Move the mouse like a real user.
- **Scroll Position Management**: Get or reset the current scroll position.
- **Retries**: Automatically retry actions if they fail with customizable delay and retry limits.
- **Validation**: Built-in validation for scrolling percentages and typing speeds.

## Installation:
You can install it with **Poetry**:
```bash
poetry add humani_py
Or with pip:
pip install humani_py

Usage:
Basic Example:
python
Copy code
from humani_py import random_delay, apply_stealth, scroll_page, human_typing, get_scroll_position, reset_scroll_position

driver = webdriver.Chrome()

# Apply stealth mode
apply_stealth(driver)

# Navigate to a website
driver.get('https://example.com')

# Simulate typing in a search box
search_box = driver.find_element_by_name('q')
human_typing(search_box, "Hello World")

# Scroll naturally down the page
scroll_page(driver, direction="down", percentage=80, speed=2.0)

# Get the current scroll position
current_scroll = get_scroll_position(driver)
print(f"Current scroll position: {current_scroll}")

# Reset scroll position to the top
reset_scroll_position(driver)
Retry Example:
python
Copy code
from humani_py.utils import retry_on_failure

@retry_on_failure(retries=3, delay=2.0)
def perform_click_action(driver, element):
    """Attempt to click an element with retries."""
    element.click()

# Example usage
button = driver.find_element_by_id('submit-button')
perform_click_action(driver, button)
Scroll Handling:
python
Copy code
from humani_py.utils import get_scroll_position, reset_scroll_position

# Get the current scroll position
current_scroll = get_scroll_position(driver)
print(f"Current scroll position: {current_scroll}")

# Reset scroll position to the top
reset_scroll_position(driver)
Validation:
python
Copy code
from humani_py.utils import validate_percentage, validate_speed

# Validate scroll percentage
validate_percentage(80)

# Validate typing speed
validate_speed(1.5)
