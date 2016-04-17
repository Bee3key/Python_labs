def checkio(integ):
	return list((bin(integ))).count('1')

if __name__ == '__main__':
	assert checkio(4) == 1, "err"
	assert checkio(15) == 4, "err"
	assert checkio(1) == 1, "err"
	assert checkio(1022) == 9, "err"