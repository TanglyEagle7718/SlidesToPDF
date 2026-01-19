import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

FOLDER_NAME = 'tmp_data'

def launch_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("about:blank")
    return driver


def advance_and_capture(driver, screenshot_path):
    actions = ActionChains(driver)

    time.sleep(0.4)
    actions.send_keys(Keys.ARROW_RIGHT).perform()

    time.sleep(0.4)
    actions.send_keys(Keys.ARROW_RIGHT).perform()

    time.sleep(0.4)
    actions.send_keys(Keys.ARROW_LEFT).perform()

    time.sleep(0.6)
    driver.save_screenshot(screenshot_path)


def take_screenshots(driver):
    relativedir = os.path.join(os.getcwd(), FOLDER_NAME)
    os.mkdir(relativedir)

    def read_bytes(path):
        with open(path, "rb") as f:
            return f.read()

    prev_image = "1.png"
    prev_path = os.path.join(relativedir, prev_image)
    advance_and_capture(driver, prev_path)

    duplicate_count = 0
    last_valid_index = 1

    i = 2
    while True:
        curr_image = f"{i}.png"
        curr_path = os.path.join(relativedir, curr_image)

        advance_and_capture(driver, curr_path)

        if read_bytes(curr_path) == read_bytes(prev_path):
            duplicate_count += 1

            if duplicate_count >= 5:
                for j in range(i - duplicate_count + 1, i + 1):
                    dup_path = os.path.join(relativedir, f"{j}.png")
                    if os.path.exists(dup_path):
                        os.remove(dup_path)

                return f"{last_valid_index}.png"
        else:
            duplicate_count = 0
            last_valid_index = i
            prev_image = curr_image
            prev_path = curr_path

        i += 1

def switch_to_active_window(driver):
    handles = driver.window_handles
    if not handles:
        raise RuntimeError("No browser windows found.")
    driver.switch_to.window(handles[-1])
