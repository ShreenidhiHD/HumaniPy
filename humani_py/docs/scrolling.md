
# **Scrolling**

**`docs/scrolling.md`**:
```markdown
# Scrolling

The `scrolling` feature allows natural scrolling of a webpage, simulating human scrolling behavior.

## Functions

### `scroll_page`

Scrolls the page in a human-like manner.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.
- `direction` (str): Direction to scroll, either `"up"` or `"down"`.
- `percentage` (float): Percentage of the page to scroll (e.g., 80).
- `speed` (float): Scrolling speed.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.scrolling import scroll_page

# Scroll down 80% of the page at a speed of 2.0
scroll_page(driver, direction="down", percentage=80, speed=2.0)
