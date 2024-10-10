from fake_useragent import UserAgent
from selenium import webdriver

def apply_stealth(driver: webdriver.Chrome) -> None:
    """Applies stealth measures like changing user-agent, headers, and other settings."""
    ua = UserAgent()
    user_agent = ua.random
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
