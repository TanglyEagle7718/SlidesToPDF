# SlidesToPDF

Tool to convert your google slideshow to a PDF. Typically, when you download your slideshow as a pdf, the transitions that you have in your presentation will overlap on top of each other. This tool aims to solve this problem.

## Running it locally

### Setting up dependencies

### Using the given environment

For this project is maintained with the poetry package manager. Before you being, make sure that you have pipx and Poetry installed:

Instructions to install pipx: https://pipx.pypa.io/stable/installation/

Instructions to install Poetry: https://python-poetry.org/docs/

Once you have Poetry installed, clone this repo to your machine w/ `git clone`

Activate your environment: `poetry shell`

Once you have activated your environment, install the necessary requirements:
`poetry install --no-root` 

Once you have done all these steps, you are done setting up your environment

### Using your own environment

If you don't want to use the poetry environment, you can install the dependencies yourself. This project only has two dependencies:

1. selenium
2. pillow

### Running it

Once you are in the virtual env, you can run the program w/ `python3 driver.py` You will notice that it throws an error

`driver.py` takes in two arguments: `-u / --url` and `-n / --name`:
- `-u / --url`: You need to specify the url to the first slide in your google slideshow. If you would like the final pdf to start at a specific slide, then navigate to that slide and use the url associated with it.
- `-n / --name`: This is the name of the final pdf output. The file must end with a `.pdf` extension

  Once you successfully run the program, the pdf with the name you set will appear in your directory
