import random
from selenium.webdriver import ActionChains
from selenium import webdriver

def random_mouse_move(driver: webdriver.Chrome, element) -> None:
    """Simulates random mouse movement to a given element."""
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, random.randint(0, 5), random.randint(0, 5))
    action.perform()
