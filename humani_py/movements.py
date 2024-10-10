import random
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from math import pow, sqrt

def ease_in_out(t: float) -> float:
    """Applies acceleration and deceleration for smooth mouse movements."""
    return 4 * t * t * t if t < 0.5 else (t - 1) * (2 * t - 2) * (2 * t - 2) + 1

def bezier_curve(t: float, P0: tuple, P1: tuple, P2: tuple, P3: tuple) -> tuple:
    """Generates a point along a cubic Bezier curve."""
    x = (pow(1 - t, 3) * P0[0] + 3 * pow(1 - t, 2) * t * P1[0] + 3 * (1 - t) * pow(t, 2) * P2[0] + pow(t, 3) * P3[0])
    y = (pow(1 - t, 3) * P0[1] + 3 * pow(1 - t, 2) * t * P1[1] + 3 * (1 - t) * pow(t, 2) * P2[1] + pow(t, 3) * P3[1])
    return x, y

def adjust_speed(distance: float) -> float:
    """Adjusts the speed of the mouse based on the distance to the target."""
    if distance < 50:
        return random.uniform(0.1, 0.2)  # Short distances have slower speeds.
    elif distance < 200:
        return random.uniform(0.2, 0.5)  # Moderate speed for medium distances.
    else:
        return random.uniform(0.5, 1.0)  # Long distances use faster speeds.

def random_mouse_move(driver: WebDriver, element: WebElement, 
                      overshoot: bool = True, easing: bool = True, 
                      random_pauses: bool = True, speed: float = 1.0,
                      test_mode: bool = False) -> None:
    """
    Simulates human-like mouse movement to an element using Bezier curves.

    Parameters:
    - driver (WebDriver): The WebDriver instance controlling the browser.
    - element (WebElement): The element to move the mouse towards.
    - overshoot (bool): Adds an overshoot effect when moving the mouse (default: True).
    - easing (bool): Enables smooth acceleration and deceleration (default: True).
    - random_pauses (bool): Adds small random pauses to simulate human hesitation (default: True).
    - speed (float): The base speed of the mouse movement (default: 1.0).
    - test_mode (bool): Disables randomness for testing (default: False).
    """
    
    # Get the target element's location on the page
    target_x = element.location['x']
    target_y = element.location['y']
    
    # Get the current mouse position (use viewport center as starting point)
    current_x, current_y = driver.execute_script("return [window.pageXOffset + window.innerWidth / 2, window.pageYOffset + window.innerHeight / 2];")

    # Calculate the distance to the target
    distance = sqrt(pow(target_x - current_x, 2) + pow(target_y - current_y, 2))

    # Adjust speed based on the distance to the target
    if test_mode:
        movement_speed = 0.01  # Fixed speed for test mode
    else:
        movement_speed = adjust_speed(distance) * speed

    # Set control points for the Bezier curve
    if test_mode:
        control_point_1 = (current_x + 10, current_y + 10)
        control_point_2 = (target_x - 10, target_y - 10)
        overshoot_distance = 10 if overshoot else 0  # Fixed overshoot for test mode
    else:
        control_point_1 = (current_x + random.randint(10, 100), current_y + random.randint(10, 100))
        control_point_2 = (target_x - random.randint(10, 100), target_y - random.randint(10, 100))
        overshoot_distance = random.uniform(5, 15) if overshoot else 0

    # Apply overshoot behavior (slightly move past the target)
    if overshoot:
        target_x += overshoot_distance
        target_y += overshoot_distance

    # Move the mouse along the Bezier curve in small steps
    steps = 100  # Define the number of increments
    for step in range(steps):
        t = step / steps
        if easing:
            t = ease_in_out(t)
        next_x, next_y = bezier_curve(t, (current_x, current_y), control_point_1, control_point_2, (target_x, target_y))
        
        # Move the mouse to the next position
        driver.execute_script(f"window.scrollBy({next_x - current_x}, {next_y - current_y});")
        current_x, current_y = next_x, next_y

        # Introduce random pauses during movement
        if not test_mode and random_pauses and random.random() > 0.97:
            time.sleep(random.uniform(0.1, 0.3))  # Short random pause

        # Adjust speed with each movement
        time.sleep(movement_speed)

    # Correct for overshoot by moving back slightly
    if overshoot:
        driver.execute_script(f"window.scrollBy({-overshoot_distance}, {-overshoot_distance});")

    # Finally, hover over the target element to simulate a real user before interacting
    action_chains = ActionChains(driver)
    action_chains.move_to_element(element)
    action_chains.perform()

    # Optional: Add a slight delay before clicking or interacting with the element
    if not test_mode:
        time.sleep(random.uniform(0.1, 0.5))