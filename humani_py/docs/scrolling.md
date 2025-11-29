# Scrolling

# Scrolling

The `scrolling` feature allows natural scrolling of a webpage, simulating human scrolling behavior with smooth transitions and pauses.

## Functions

### `scroll_page`

Scrolls the page in a human-like manner using smooth scrolling behavior and random chunking.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.
- `direction` (str): Direction to scroll, either `"up"` or `"down"`. Default is `"down"`.
- `percentage` (float): Percentage of the page to scroll (0-100). Default is `100`.
- `speed` (float): Scrolling speed multiplier. Higher values result in slower scrolling. Default is `1.0`.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.scrolling import scroll_page

# Scroll down 80% of the page at a relaxed speed
scroll_page(driver, direction="down", percentage=80, speed=2.0)
```
