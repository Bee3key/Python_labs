ops = {
    'conjunction': lambda x, y: x & y,
    'disjunction': lambda x, y: x | y,
    'implication': lambda x, y: (1 - x) | y,
    'exclusive': lambda x, y: x ^ y, 
    'equivalence': lambda x, y: x == y }


def boolean(x,y, name):
	return ops[name](x, y)

if __name__ == '__main__':
	print (boolean(1, 0, "conjunction"))
	print (boolean(0, 1, "implication"))
