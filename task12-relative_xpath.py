from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
url = "https://www.guvi.in/"
driver.get(url)
time.sleep(5)  # Wait for page to load

# --- XPATH EXAMPLES ---
# Example element (the red underlined element in your image)
# Based on ANI news structure, we'll pick a popular headline
red_underlined_element = "(//h3[contains(@class, 'h5')])[1]"

try:
    # 3. Relative Path Tasks
    # A) Find the "parent" element
    parent_el = driver.find_element(By.XPATH, f"{red_underlined_element}/parent::*")
    print(f"Parent Element Tag: {parent_el.tag_name}")

    # B) Find the first "child" element of that parent
    child_el = driver.find_element(By.XPATH, f"{parent_el.xpath}/child::*[1]")
    print(f"First Child Element Tag: {child_el.tag_name}")

    # C) Locate the second sibling (if any)
    second_sibling = driver.find_element(By.XPATH, f"{red_underlined_element}/following-sibling::*[2]")
    print(f"Second Sibling Tag: {second_sibling.tag_name}")

    # D) Select the parent element of element with attribute 'href'
    parent_of_href = driver.find_element(By.XPATH, "//a[@href]/parent::*")
    print(f"Parent of href: {parent_of_href.tag_name}")

    # 4. Axes Tasks
    # A) Find all ancestor elements
    ancestors = driver.find_elements(By.XPATH, f"{red_underlined_element}/ancestor::*")
    print(f"Number of Ancestors: {len(ancestors)}")

    # B) Locate all following siblings
    following_siblings = driver.find_elements(By.XPATH, f"{red_underlined_element}/following-sibling::*")
    print(f"Following Siblings Count: {len(following_siblings)}")

    # C) Select all preceding elements
    preceding_elements = driver.find_elements(By.XPATH, f"{red_underlined_element}/preceding::*")
    print(f"Preceding Elements Count: {len(preceding_elements)}")

finally:
    driver.quit()
