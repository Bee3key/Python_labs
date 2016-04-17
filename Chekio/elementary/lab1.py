def checkio (num):
	res1 = (num/3) - (num//3)
	res2 = (num/5) - (num//5)
	if (res1 == 0 ) and (res2 == 0):
		result = "Fizz Buzz"
	elif (res1 !=0) and (res2 == 0):
		result = "Buzz"
	elif (res2 !=0) and (res1 == 0):
		result = "Fizz"
	else:
		result = str(num)
	return result
if __name__=='__main__':
	assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
	assert checkio(6) == "Fizz", "6 is divisible by 3"
	assert checkio(5) == "Buzz", "5 is divisible by 5"
	assert checkio(7) == "7", "7 is not divisible by 3 or 5"