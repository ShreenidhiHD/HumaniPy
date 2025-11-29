# HumaniPy: random_mouse_move Function

## Overview

The `random_mouse_move` function is part of the `movements` feature in HumaniPy. It simulates **true** human-like mouse movements using Bezier curves and Selenium's `ActionChains`. This replaces the older method of scrolling to elements, providing a much more realistic and undetectable interaction.

## Function Signature

```python
def random_mouse_move(
    driver: WebDriver,
    element: WebElement,
    overshoot: bool = True,
    easing: bool = True,
    random_pauses: bool = True,
    speed: float = 1.0
) -> None:
```

## Parameters

- `driver` (WebDriver): The WebDriver instance controlling the browser.
- `element` (WebElement): The target element to move the mouse to.
- `overshoot` (bool, optional): Whether to simulate overshooting the target before correcting. Default is `True`.
- `easing` (bool, optional): Adds smooth acceleration/deceleration to the movement. Default is `True`.
- `random_pauses` (bool, optional): Introduces random micro-pauses during movement to simulate human hesitation. Default is `True`.
- `speed` (float, optional): Speed multiplier. Higher values result in *slower* movement (it acts as a delay multiplier). Default is `1.0`.

## Return Value

- `None`

## Description

The `random_mouse_move` function calculates a natural, curved path from the current mouse position (or a random start point) to the target element. It uses cubic Bezier curves to generate the path and `ActionChains` to perform the movement in small increments.

## Example Usage

```python
from humani_py.movements import random_mouse_move

# Move the mouse to the specific element with natural behavior
random_mouse_move(driver, target_element, overshoot=True, speed=1.0)
target_element.click()
```