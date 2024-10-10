from fake_useragent import UserAgent
from selenium import webdriver

def apply_stealth(driver: webdriver.Chrome, test_mode=False) -> None:
    """Applies stealth measures like changing user-agent, headers, and other settings."""
    if test_mode:
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"
    else:
        ua = UserAgent()
        user_agent = ua.random
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})