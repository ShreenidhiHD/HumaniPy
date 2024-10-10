# Utilities

The utils module provides helper functions for common tasks in HumaniPy.

## Functions

### get_scroll_position

Returns the current scroll position of the page.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.

#### Returns:
- `int`: Current scroll position in pixels.

#### Example Usage:
```python
from humani_py.utils import get_scroll_position

# Get the current scroll position
current_scroll = get_scroll_position(driver)
print(f"Current scroll position: {current_scroll}")
```

### reset_scroll_position

Resets the scroll position to the top of the page.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.utils import reset_scroll_position

# Reset scroll position to the top
reset_scroll_position(driver)
```