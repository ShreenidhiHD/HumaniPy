# HumaniPy: random_mouse_move Function

## Overview

The `random_mouse_move` function is part of the `movements` feature in HumaniPy. It simulates human-like mouse movements, designed to mimic real user interactions when automating web browsing.

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
- `overshoot` (bool, optional): Whether to simulate overshooting the target. Default is `True`.
- `easing` (bool, optional): Adds smooth acceleration/deceleration. Default is `True`.
- `random_pauses` (bool, optional): Introduces random pauses during movement. Default is `True`.
- `speed` (float, optional): Base speed of the mouse movement. Default is `1.0`.

## Return Value

- `None`

## Description

The `random_mouse_move` function simulates natural mouse movements to a given element. It includes options for overshooting the target, applying easing effects, and introducing random pauses to make the movement appear more human-like.

## Example Usage

```python
from humani_py.movements import random_mouse_move

# Assuming you have already set up your WebDriver and found your target element
driver = # ... your WebDriver instance
target_element = # ... your target WebElement

# Move the mouse to the specific element with natural behavior
random_mouse_move(driver, target_element, overshoot=True, easing=True, random_pauses=True, speed=1.0)
```

This example demonstrates how to use the `random_mouse_move` function to simulate a human-like mouse movement to a specific web element.

## Notes

- This function is particularly useful for automating web interactions in a way that mimics human behavior.
- It can help in avoiding detection by anti-bot systems that look for perfectly straight or unnaturally fast mouse movements.
- Adjusting the `speed` parameter allows for fine-tuning the overall speed of the mouse movement.