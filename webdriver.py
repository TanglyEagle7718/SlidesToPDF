import os
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from exceptions import InvalidURL

FOLDER_NAME = 'tmp_data'

def validate_url(url: str) -> str:
	regex = r'(https:\/\/)?docs\.google\.com\/presentation\/d\/.*\/(edit|present).*'
	if re.match(regex, url):
		new_url = re.sub(r'(?<=)(edit)', 'present', url)
		return new_url 
	else:
		#parkChrome()
		raise InvalidURL()

def take_screenshots(driver):
	# creates a tmp_data folder
	relativedir = os.path.join(os.getcwd(), FOLDER_NAME)
	os.mkdir(relativedir)
	
	# create first image
	prev_image = '1.png' 
	screenshot_path = os.path.join(relativedir, prev_image)
	driver.save_screenshot(str(screenshot_path))
	ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()

	curr_image = "2.png"
	screenshot_path = os.path.join(relativedir, curr_image)
	driver.save_screenshot(str(screenshot_path))
	ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()

	i = 3
	prev_image_path = os.path.join(relativedir, prev_image)
	curr_image_path = os.path.join(relativedir, curr_image)
	while open(prev_image_path, 'rb').read() != open(curr_image_path, 'rb').read():
		prev_image = curr_image
		prev_image_path = os.path.join(relativedir, prev_image)
		curr_image = f"{i}.png"
		curr_image_path = os.path.join(relativedir, curr_image)
		driver.save_screenshot(str(curr_image_path))
		ActionChains(driver).key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
		i+=1
	return prev_image

def driveChrome(url: str) -> str:
	url = validate_url(url)
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get(url)
	return take_screenshots(driver)