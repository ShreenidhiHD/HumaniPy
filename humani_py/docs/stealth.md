# Stealth

# Stealth Mode

The `stealth` feature makes the automation more difficult to detect by applying various evasion techniques.

## Functions

### `apply_stealth`

Applies stealth modifications to the WebDriver instance to mask automation signals.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.
- `test_mode` (bool, optional): If `True`, uses a fixed user agent for testing. Default is `False`.

#### What it does:
1.  **User Agent**: Rotates the User-Agent string using `fake-useragent`.
2.  **WebDriver Property**: Hides the `navigator.webdriver` property using CDP commands.
3.  **Window Size**: Randomizes the window size and position slightly to prevent fingerprinting based on standard resolutions.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.stealth import apply_stealth

# Apply stealth to avoid detection
apply_stealth(driver)
```
