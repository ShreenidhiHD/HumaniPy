from selenium import webdriver
import time

def scroll_page(driver: webdriver.Chrome, direction: str = "down", percentage: int = 100, speed: float = 1.0) -> None:
    """Scrolls the page slowly in a given direction with randomized behavior."""
    scroll_amount = (percentage / 100) * driver.execute_script("return document.body.scrollHeight")
    scroll_by = scroll_amount if direction == "down" else -scroll_amount
    driver.execute_script(f"window.scrollBy(0, {scroll_by});")
    time.sleep(speed)
