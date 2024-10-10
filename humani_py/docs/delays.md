# Delays

The `delays` feature in HumaniPy provides random delays that simulate human-like hesitations. 

## Functions

### `random_delay`

This function helps add a random delay to mimic human hesitation.

#### Parameters:
- `min_delay` (float): Minimum time to wait, in seconds.
- `max_delay` (float): Maximum time to wait, in seconds.

#### Returns:
- `None`

#### Example Usage:
```python
from humani_py.delays import random_delay

# Add a delay between 1 and 3 seconds
random_delay(min_delay=1.0, max_delay=3.0)
