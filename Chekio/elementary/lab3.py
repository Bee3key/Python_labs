a = [0, 1, 2, 3, 4, 5]
b = [1, 3, 5]
c = [6]
d = [0]

def checkio (list):
	try:
		last_num = list[(len(list) -1)]
		return sum(list[::2])*last_num
	except Exception:
		return 0
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"