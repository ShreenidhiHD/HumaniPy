from selenium.common.exceptions import WebDriverException

def handle_webdriver_exception(func):
    """Decorator to catch and handle WebDriver exceptions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except WebDriverException as e:
            print(f"WebDriverException occurred: {e}")
            raise e
    return wrapper

def validate_percentage(value: int) -> bool:
    """Validate that a percentage value is between 0 and 100."""
    if not (0 <= value <= 100):
        raise ValueError(f"Invalid percentage: {value}. Must be between 0 and 100.")
    return True

def validate_speed(value: float) -> bool:
    """Validate that speed values are positive."""
    if value <= 0:
        raise ValueError(f"Invalid speed: {value}. Must be positive.")
    return True

def get_scroll_position(driver) -> int:
    """Returns the current vertical scroll position of the page."""
    return driver.execute_script("return window.pageYOffset;")

def reset_scroll_position(driver) -> None:
    """Resets the scroll position to the top of the page."""
    driver.execute_script("window.scrollTo(0, 0);")

def retry_on_failure(retries: int = 3, delay: float = 1.0):
    """Retry decorator to re-attempt a function after a delay if it fails."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            # If all attempts fail, raise the last exception
            raise last_exception
        return wrapper
    return decorator
