from fake_useragent import UserAgent
from selenium import webdriver
import random

def apply_stealth(driver: webdriver.Chrome, test_mode=False) -> None:
    """Applies stealth measures like changing user-agent, headers, and other settings."""
    if test_mode:
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
    else:
        ua = UserAgent()
        user_agent = ua.random
        
    # Override User Agent
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
    
    # Hide WebDriver property
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    
    # Randomize window size slightly to avoid fingerprinting
    if not test_mode:
        width = random.randint(1024, 1920)
        height = random.randint(768, 1080)
        driver.set_window_size(width, height)
        
        # Randomize window position
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        driver.set_window_position(x, y)