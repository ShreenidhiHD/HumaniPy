import random
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def random_mouse_move(driver: WebDriver, element: WebElement, test_mode: bool = False) -> None:
    """Simulates random mouse movement to a given element."""
    action = ActionChains(driver)
    if test_mode:
        x_offset, y_offset = 0, 0
    else:
        x_offset, y_offset = random.randint(0, 5), random.randint(0, 5)
    
    action.move_to_element_with_offset(element, x_offset, y_offset).perform()

    
    # Perform the action
    action.perform()