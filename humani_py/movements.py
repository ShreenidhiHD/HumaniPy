import random
from selenium.webdriver import ActionChains
from selenium import webdriver

def random_mouse_move(driver: webdriver.Chrome, element, test_mode=False) -> None:
    """Simulates random mouse movement to a given element."""
    action = ActionChains(driver)
    if test_mode:
        x_offset, y_offset = 0, 0
    else:
        x_offset, y_offset = random.randint(0, 5), random.randint(0, 5)
    action.move_to_element_with_offset(element, x_offset, y_offset)
    action.perform()