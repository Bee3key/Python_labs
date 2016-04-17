"""
net__ = ((1, 0, 0, 1, 0),
		(0, 1, 0, 0, 0),
		(0, 0, 1, 0, 1),
		(1, 0, 0, 0, 0),
		(0, 0, 1, 0, 0),)

def count_neighbours(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))
    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))
    
    return sum(grid[ro][co] for ro in rows for co in cols) - grid[row][col]

kordX = элементы - строки
kordY = элементы строк
"""

arr = (  (1, 1, 0, 0, 0),
		 (1, 0, 0, 0, 0),
		 (0, 0, 1, 0, 1),
		 (1, 0, 0, 0, 0),
		 (0, 0, 1, 0, 0),)

def count_neighbours(net__, kordX, kordY):
	try:
		Xs = range(max(0, kordX - 1), min(kordX + 2, len(net__)))
		Ys = range(max(0, kordY - 1), min(kordY + 2, len(net__[0])))
		result = sum(net__[x][y] for x in Xs for y in Ys) - net__[kordX][kordY]
	except LookupError:
		result = -1
	return result
  

if __name__ == '__main__':
	print ([arr[i][j] for i in range(0,len(arr)) for j in range (0,len(arr[0]))])