import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from humani_py.movements import random_mouse_move
from humani_py.typing import human_typing
from humani_py.scrolling import scroll_page
from humani_py.stealth import apply_stealth
import time

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Run headless for CI/CD environments
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_stealth_application(driver):
    apply_stealth(driver, test_mode=True)
    driver.get("data:text/html,<html><body><h1>Stealth Test</h1></body></html>")
    assert "Stealth Test" in driver.page_source

def test_typing_simulation(driver):
    driver.get("data:text/html,<html><body><input type='text' id='input'></body></html>")
    input_box = driver.find_element(By.ID, "input")
    text_to_type = "Hello World"
    human_typing(input_box, text_to_type, min_speed=0.01, max_speed=0.02)
    assert input_box.get_attribute("value") == text_to_type

def test_mouse_movement(driver):
    # Ensure body has size so we can move relative to it
    driver.get("data:text/html,<html><body style='width:1000px; height:1000px;'><button id='btn' style='position:absolute; left:100px; top:100px;'>Click Me</button></body></html>")
    btn = driver.find_element(By.ID, "btn")
    # This should not raise an exception
    random_mouse_move(driver, btn, test_mode=True)

def test_scrolling(driver):
    # Create a long page
    driver.get("data:text/html,<html><body><div style='height:2000px;'>Long Page</div></body></html>")
    scroll_page(driver, direction="down", percentage=50, speed=0.1)
    # Check if we scrolled
    scroll_y = driver.execute_script("return window.pageYOffset;")
    assert scroll_y > 0
