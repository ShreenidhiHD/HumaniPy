
# Typing

**`docs/typing.md`**:
```markdown
# Typing Simulation

The `typing` feature simulates human typing with random keystrokes to make automation look natural.

## Functions

### `human_typing`

Simulates typing text into a given input field, mimicking human typing speed and errors.

#### Parameters:
- `input_element` (WebElement): The input element to type in.
- `text` (str): The text to type.
- `speed` (float, optional): Typing speed in seconds per character.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.typing import human_typing

# Type "Hello World" into a search box
human_typing(search_box, "Hello World")
