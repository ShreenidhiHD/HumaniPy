# Movements

The `movements` feature in HumaniPy simulates human-like mouse movements.

## Functions

### `human_mouse_move`

Simulates a human-like mouse movement to the specified target position.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.
- `target_element` (WebElement): The target element to move the mouse to.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.movements import human_mouse_move

# Move the mouse to a specific element
human_mouse_move(driver, target_element)
