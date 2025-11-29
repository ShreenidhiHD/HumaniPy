# HumaniPy

[![PyPI version](https://badge.fury.io/py/humani_py.svg)](https://badge.fury.io/py/humani_py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/ShreenidhiHD/HumaniPy/actions/workflows/python-tests.yml/badge.svg)](https://github.com/ShreenidhiHD/HumaniPy/actions/workflows/python-tests.yml)

> "Because even your bots deserve to act a little more human."

**HumaniPy** is a Python package designed to make web automation undetectable and human-like. It provides advanced utilities for mouse movements, typing, scrolling, and stealth, ensuring your bots behave like real users.

## 🚀 Features

- **True Mouse Movements**: Simulates realistic cursor paths using Bezier curves and `ActionChains`.
- **Enhanced Stealth**: Automatically hides `navigator.webdriver` and randomizes window dimensions.
- **Natural Typing**: Types with variable speeds and simulates occasional typos with corrections.
- **Smooth Scrolling**: Scrolls pages naturally with smooth behavior and random pauses.
- **Robustness**: Built-in retry mechanisms and error handling.

## 📦 Installation

Install HumaniPy via pip:

```bash
pip install humani_py
```

## 🛠 Usage

### Quick Start

```python
from selenium import webdriver
from humani_py.stealth import apply_stealth
from humani_py.typing import human_typing
from humani_py.scrolling import scroll_page
from humani_py.movements import random_mouse_move
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 1. Apply stealth settings immediately
apply_stealth(driver)

driver.get('https://www.google.com')

# 2. Simulate human typing
search_box = driver.find_element(By.NAME, "q")
human_typing(search_box, "HumaniPy automation")

# 3. Move mouse naturally to an element
random_mouse_move(driver, search_box)

# 4. Scroll the page like a human
scroll_page(driver, direction="down", percentage=50)
```

## 📄 Documentation

For full documentation, visit our [GitHub Pages](https://shreenidhihd.github.io/HumaniPy/).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.