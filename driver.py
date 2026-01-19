import argparse
import os
import pdf_utils
import shutil

import pdf_driver
import webdriver

DEBUG = 0
FOLDER_NAME = webdriver.FOLDER_NAME

def main():
    parser = argparse.ArgumentParser(
        description="Convert a PowerPoint presentation opened in Chromium into a PDF.\n"
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        help='Enter name of final pdf file',
        required=True
    )
    
    parser.add_argument(
        '--trim-end',
        type=int,
        default=0,
        help='Remove N slides from the end of the final PDF'
    )


    pdf_file_name = parser.parse_args().name
    trim_end = parser.parse_args().trim_end

    if not pdf_file_name.endswith(".pdf"):
        raise ValueError("Output file must be a .pdf")

    print("Launching Chromium browser...")
    driver = webdriver.launch_chrome()

    print(
        "\nPlease upload and open your PowerPoint presentation in the browser.\n"
        "Navigate to the first slide and switch to presentation mode.\n"
        "When ready, return here and type 'yes' to begin capture."
    )

    while True:
        user_input = input("> ").strip().lower()
        if user_input == "yes":
            break
        print("Type 'yes' to continue.")

    print("Starting screenshot capture...")
    webdriver.switch_to_active_window(driver)
    
    last_image = webdriver.take_screenshots(driver)
    
    print("Creating PDF...")
    pdf_driver.combine_to_pdf(last_image, pdf_file_name)

    if trim_end > 0:
        print(f"Removing last {trim_end} slides from PDF...")
        pdf_utils.trim_pages_from_end(pdf_file_name, trim_end)



def cleanup():
    folder_path = os.path.join(os.getcwd(), FOLDER_NAME)
    if os.path.isdir(folder_path):
        shutil.rmtree(folder_path)

def switch_to_active_window(driver):
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
        print("exited gracefully")
