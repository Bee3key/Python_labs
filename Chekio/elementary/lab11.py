import string

def check_pangram(text):
	return all(letter in text.lower() for letter in string.ascii_lowercase[:26])
print (check_pangram("The quick brown fox jumps over the lazy dog."))