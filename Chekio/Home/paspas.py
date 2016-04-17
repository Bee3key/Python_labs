import re


def checkio(mypass):
	if len(mypass) >= 10 and re.search("\d", mypass) and re.search("[a-z]", mypass) and re.search("[A-Z]", mypass):
		result = True
	else:
		result = False
	return result

print (checkio('A1213pokl'))
print (checkio('bAse730onE')) 
print (checkio('asasasasasasasaas'))
print (checkio('QWERTYqwerty'))
print (checkio('123456123456'))
print (checkio('QwErTy911poqqqq'))