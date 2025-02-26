
class InvalidURL(Exception):
	def __str__(self):
		return "Invalid URL inputted. Must be a google slides url"

class InvalidFileName(Exception):
	def __str__(self):
		return "Invalid file name"