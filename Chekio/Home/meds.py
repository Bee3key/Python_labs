def checkio(intArr):
	sorted_arr = sorted(intArr)
	print (sorted_arr)
	ll = len(sorted_arr)
	print (ll)
	if ll%2 == 0:
		result = (sorted_arr[int(ll/2)] + sorted_arr [int(ll/2 - 1)]) / 2
	elif ll%2 == 1:
		result = sorted_arr[int(round(ll/2))]
		print (int((ll/2)))
	return result
	

print (checkio([10,9,8,7,6,5,4,3,2,1,0]))

"""
checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5
"""
