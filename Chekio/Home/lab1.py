def checkio(array):
	return [i for i in array if array.count(i) == 1]

if __name__ == '__main__':
	print (checkio([1, 2, 3, 1, 3]))
	assert checkio([1, 2, 3, 4, 5]) == [], "err"
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "err"
	assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "err"