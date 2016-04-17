import time
from datetime import datetime
"""
firstD = 1982, 4, 19
secondD = 1982, 4, 22
fy, fm, fd = firstD
sy, sm, sd = secondD
print (int((str((abs(datetime.date(datetime(fy, fm, fd)) - datetime.date(datetime(sy, sm, sd))))).split())[0]))
"""

def days_diff(firstD, secondD):
		fy, fm, fd = firstD
		sy, sm, sd = secondD
		return abs(datetime.date(datetime(fy, fm, fd)) - datetime.date(datetime(sy, sm, sd))).days
if __name__ == '__main__':
	assert days_diff((2014,2,28), (2014,2,28)) == 0, "err"
	days_diff((1982, 4, 19), (1982, 4, 22)) 
	days_diff((2014, 1, 1), (2014, 8, 27)) 
	days_diff((2014, 8, 27), (2014, 1, 1)) 
