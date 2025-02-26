import argparse
import os
import shutil

import pdf_driver
import webdriver

DEBUG = 0 # 0 means prod, 1 for dev
FOLDER_NAME = webdriver.FOLDER_NAME

def main():
	global DEBUG
	parser = argparse.ArgumentParser(description="Convert your Google Slides to a proper PDF. \nUse '-u' argument to direct link to google slideshow. \nUse '-n' argument to set the name of your output pdf\n")
    
	if not DEBUG:
		parser.add_argument('-u', '--url', type=str, help='Enter target google slides url (should have open sharing perms)', required=True)
		parser.add_argument('-n', '--name', type=str, help='Enter name of final pdf file', required=True)
		url = parser.parse_args().url
		pdf_file_name = parser.parse_args().name

	else:
		url = "[test_url]"
		pdf_file_name = "test.pdf"
    
	print(f"Navigating to {url}!")
	last_image = webdriver.driveChrome(url)
	pdf_driver.combine_to_pdf(last_image, pdf_file_name)


def cleanup():

	# Specify the folder name relative to the current directory
	global FOLDER_NAME

	# Construct the full path to the folder
	folder_path = os.path.join(os.getcwd(), FOLDER_NAME)
	if os.path.isdir(folder_path):
		shutil.rmtree(folder_path)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
	finally:
		cleanup()
		print("exited gracefully")
