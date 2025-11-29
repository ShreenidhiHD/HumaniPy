# Typing

# Typing Simulation

The `typing` feature simulates human typing with random keystrokes, variable speeds, and occasional typos to make automation look natural.

## Functions

### `human_typing`

Simulates typing text into a given input field, mimicking human typing speed and errors.

#### Parameters:
- `element` (WebElement): The input element to type in.
- `text` (str): The text to type.
- `min_speed` (float, optional): Minimum delay between keystrokes in seconds. Default is `0.05`.
- `max_speed` (float, optional): Maximum delay between keystrokes in seconds. Default is `0.2`.
- `typo_chance` (float, optional): Probability (0.0 to 1.0) of making a typo per character. Default is `0.05`.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.typing import human_typing

# Type "Hello World" with a slight chance of typos
human_typing(search_box, "Hello World", min_speed=0.05, max_speed=0.15, typo_chance=0.1)
```
