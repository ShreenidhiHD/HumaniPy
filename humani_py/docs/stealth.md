
# Stealth

```markdown
# Stealth Mode

The `stealth` feature makes the automation more difficult to detect by changing headers, user-agent, etc.

## Functions

### `apply_stealth`

Applies stealth modifications to the WebDriver instance.

#### Parameters:
- `driver` (WebDriver): The WebDriver instance.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.stealth import apply_stealth

# Apply stealth to avoid detection
apply_stealth(driver)
