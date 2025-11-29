import random
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from math import pow

def ease_in_out(t: float) -> float:
    """Applies acceleration and deceleration for smooth mouse movements."""
    return 4 * t * t * t if t < 0.5 else (t - 1) * (2 * t - 2) * (2 * t - 2) + 1

def bezier_curve(t: float, P0: tuple, P1: tuple, P2: tuple, P3: tuple) -> tuple:
    """Generates a point along a cubic Bezier curve."""
    x = (pow(1 - t, 3) * P0[0] + 3 * pow(1 - t, 2) * t * P1[0] + 3 * (1 - t) * pow(t, 2) * P2[0] + pow(t, 3) * P3[0])
    y = (pow(1 - t, 3) * P0[1] + 3 * pow(1 - t, 2) * t * P1[1] + 3 * (1 - t) * pow(t, 2) * P2[1] + pow(t, 3) * P3[1])
    return x, y

def random_mouse_move(driver: WebDriver, element: WebElement, 
                      overshoot: bool = True, easing: bool = True, 
                      random_pauses: bool = True, speed: float = 1.0,
                      test_mode: bool = False) -> None:
    """
    Simulates human-like mouse movement to an element using Bezier curves and ActionChains.
    """
    
    # Get target element center
    rect = element.rect
    target_x = rect['x'] + rect['width'] / 2
    target_y = rect['y'] + rect['height'] / 2
    
    # Get current mouse position (simulated)
    # Note: Selenium doesn't expose current mouse position easily without tracking it.
    # We'll assume starting from a random position or 0,0 if not tracked.
    # For better realism in a real session, one might track the last known position.
    # Here we simulate a start point relative to the viewport or just move from "current".
    # Since ActionChains moves are relative or to an element, we'll use move_to_element with offsets
    # to simulate the path.
    
    # However, standard ActionChains doesn't let us "move to x,y" absolute easily without a reference.
    # We will simulate the *visual* path by moving in small increments relative to the *start* element 
    # if we had one, but here we are moving TO an element.
    # A common strategy is to move to the element directly with ActionChains, but that's instant.
    # To do it slowly, we need to hack it a bit or use a library that supports it.
    # Given the constraints, we will implement a "series of small moves" towards the target.
    
    # LIMITATION: Without knowing the current mouse position, we can't draw a perfect curve from A to B.
    # We will assume the mouse is at (0,0) or top-left of viewport for the sake of the curve calculation,
    # OR we can just perform the "hover" with a delay.
    # BUT, to respect the "human-like" goal, let's try to fake a path.
    
    # Let's assume we start from some random point in the viewport if we can't determine it.
    viewport_width = driver.execute_script("return window.innerWidth;")
    viewport_height = driver.execute_script("return window.innerHeight;")
    
    start_x = random.randint(0, viewport_width)
    start_y = random.randint(0, viewport_height)
    
    # Control points
    if test_mode:
        control_point_1 = (start_x + 10, start_y + 10)
        control_point_2 = (target_x - 10, target_y - 10)
    else:
        control_point_1 = (start_x + random.randint(-100, 100), start_y + random.randint(-100, 100))
        control_point_2 = (target_x + random.randint(-100, 100), target_y + random.randint(-100, 100))

    actions = ActionChains(driver)
    
    # We can't easily "teleport" the mouse to start_x, start_y without an element reference.
    # So we will simplify: We will move to the element with a delay and some "jitter" if possible.
    # Actually, w3c actions allow pointer moves to coordinates.
    # Let's use the lower-level w3c actions if possible, or stick to a robust ActionChains approach.
    # For this "robust" version, we'll implement the curve by moving to absolute coordinates using the body as reference.
    
    body = driver.find_element("tag name", "body")
    
    steps = 20 if test_mode else random.randint(20, 50)
    
    # Move to start position first (instant)
    actions.move_to_element_with_offset(body, int(start_x), int(start_y)).perform()
    
    for step in range(steps):
        t = step / steps
        if easing:
            t = ease_in_out(t)
            
        next_x, next_y = bezier_curve(t, (start_x, start_y), control_point_1, control_point_2, (target_x, target_y))
        
        # Move to the next point
        # Note: move_to_element_with_offset is from the top-left of the element (body)
        try:
            actions.move_to_element_with_offset(body, int(next_x), int(next_y)).perform()
        except Exception:
            # If out of bounds, ignore
            pass
            
        # Sleep to simulate speed
        if not test_mode:
            time.sleep(random.uniform(0.001, 0.01) / speed)
            
    # Final move to the actual element to ensure we are focused on it
    actions.move_to_element(element).perform()
    
    if not test_mode and random_pauses:
        time.sleep(random.uniform(0.1, 0.3))