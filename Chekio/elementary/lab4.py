stri = "hello world!"
def find_message(string):
	new_list = []
	for i in list(string):
		if i.isupper():
			new_list.append(i)
	return "".join(new_list)

print (find_message(stri))	
