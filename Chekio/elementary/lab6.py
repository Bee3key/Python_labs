def checkio (*args):
	num_arr = []
	for item in args:
		num_arr.append(item)
	if len(num_arr) > 0:
		return round((max(num_arr) - min(num_arr)),1)
	else:
		return 0


assert checkio(1, 2, 3) == 2, "error"
assert checkio(5, -5) == 10, "error"
#assert checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4, "error"
print(checkio(10.2, -2.2, 0, 1.1, 0.5))
assert checkio() == 0, "error"