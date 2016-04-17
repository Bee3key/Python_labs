def checkio(string):
	get_list = string.split()
	count = 0
	for word in get_list:
		if word.isalpha():
			count +=1
		elif word.isalnum():
			if count < 3:
				count = 0
			else:
				break
	if count >= 3:
		return True
	else:
		return False
if __name__ == '__main__':
	assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "error"
