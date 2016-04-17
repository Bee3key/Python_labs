import collections
def checkio(astring):
    acollection = collections.Counter()
    thestring= list(i for i in astring.lower() if i.isalpha())
	
	#count every letter in the list
    for aletter in thestring:
        acollection[aletter] += 1

    sorted_collection = sorted(list(zip(acollection.values(), acollection.keys())), key =lambda it: it[1], reverse=True)
    
    lettersum = sorted_collection[0][1]
    letter = sorted_collection[0][0]
	
    for anitem in sorted_collection:
        if anitem[1] < lettersum: break
        if anitem[0] < letter: letter = anitem[0]
    print (letter)
    
    
	
if __name__ == '__main__':
    checkio("Hello World!")
    checkio("AAAAoooo")
    checkio("How do you do?")

