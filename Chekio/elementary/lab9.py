def checkio(num):
	n = 1
	for item in list(str(num)) :
		if int(item) !=0 :
			n = int(item)*n
	return n 
checkio (123405)
checkio(999) 
checkio(1000)
checkio(1111)