from selenium import webdriver
import time
import random

def scroll_page(driver: webdriver.Chrome, direction: str = "down", percentage: int = 100, speed: float = 1.0) -> None:
    """
    Scrolls the page with randomized behavior to mimic human scrolling.
    
    Parameters:
    - driver: WebDriver instance.
    - direction: "down" or "up".
    - percentage: Percentage of the page to scroll (0-100).
    - speed: Multiplier for scroll speed (higher is slower).
    """
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")
    current_position = driver.execute_script("return window.pageYOffset")
    
    target_scroll = (percentage / 100) * (total_height - viewport_height)
    
    if direction == "up":
        target_position = max(0, current_position - target_scroll)
    else:
        target_position = min(total_height - viewport_height, current_position + target_scroll)
        
    # Break the scroll into chunks
    distance = abs(target_position - current_position)
    min_chunk = 50
    max_chunk = 200
    
    while distance > 0:
        chunk = random.randint(min_chunk, max_chunk)
        if chunk > distance:
            chunk = distance
            
        if direction == "down":
            current_position += chunk
        else:
            current_position -= chunk
            
        driver.execute_script(f"window.scrollTo({{top: {current_position}, behavior: 'smooth'}});")
        
        distance -= chunk
        
        # Random pause between chunks
        time.sleep(random.uniform(0.1, 0.3) * speed)
