a = 111
b = 3
def index_power (arr, power):
	try:
		powered_arr = arr[power]**power
	except Exception:
		powered_arr = -1
	return powered_arr
print (index_power(a,b))

		
		
