import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from humani_py.stealth import apply_stealth
from humani_py.typing import human_typing
from humani_py.scrolling import scroll_page
from humani_py.movements import random_mouse_move

def main():
    # Setup Driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Comment out to see it in action if you have a display
    driver = webdriver.Chrome(options=options)
    
    try:
        # Apply Stealth
        print("Applying stealth settings...")
        apply_stealth(driver)
        
        # Load local demo file
        file_path = os.path.abspath("demo.html")
        print(f"Loading demo page: {file_path}")
        driver.get(f"file://{file_path}")
        time.sleep(2)

        # 1. Typing Demo
        print("Demonstrating Human Typing...")
        name_input = driver.find_element(By.ID, "name-input")
        human_typing(name_input, "HumaniPy Bot", min_speed=0.05, max_speed=0.15)
        time.sleep(1)
        
        feedback_input = driver.find_element(By.ID, "feedback-input")
        human_typing(feedback_input, "This library makes automation feel so much more natural! I love the typos.", min_speed=0.03, max_speed=0.1)
        time.sleep(1)

        # 2. Mouse Movement & Click Demo
        print("Demonstrating Mouse Movement...")
        submit_btn = driver.find_element(By.ID, "submit-btn")
        random_mouse_move(driver, submit_btn)
        time.sleep(0.5)
        submit_btn.click()
        
        # Handle alert if it pops up
        try:
            time.sleep(1)
            alert = driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
        except:
            pass

        # 3. Scrolling Demo
        print("Demonstrating Natural Scrolling...")
        scroll_page(driver, direction="down", percentage=100, speed=1.5)
        time.sleep(1)

        # 4. Click Bottom Button
        print("Clicking footer button...")
        footer_btn = driver.find_element(By.ID, "footer-btn")
        random_mouse_move(driver, footer_btn)
        time.sleep(0.5)
        footer_btn.click()
        
        # Handle alert
        try:
            time.sleep(1)
            alert = driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
        except:
            pass
            
        print("Demo completed successfully!")
        time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
