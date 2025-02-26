from PIL import Image
import os

from webdriver import FOLDER_NAME

def combine_to_pdf(last_image:str, pdf_name: str):
	global FOLDER_NAME

	number_of_images = last_image.split(".")[0]
	relativedir = os.path.join(os.getcwd(), FOLDER_NAME)

	images = list()
	for i in range(1, int(number_of_images)+1):
		
		file_name = f"{i}.png"
		screenshot_path = os.path.join(relativedir, file_name)
		images.append(Image.open(screenshot_path))
	
	pdf_path = os.path.join(os.getcwd(), pdf_name)
	images[0].save(pdf_path, save_all=True, append_images=images[1:])