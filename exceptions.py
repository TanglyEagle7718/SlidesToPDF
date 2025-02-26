



class InvalidURL(Exception):
	def __str__(self):
		return "Invalid URL inputted. Must be a google slides url"
