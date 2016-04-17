__author__ = 'Bee3Key'


example = [[0, 1, 0, 1, 0, 1],
           [1, 8, 1, 0, 0, 0],
           [0, 1, 2, 0, 0, 1],
           [1, 0, 0, 9, 1, 0],
           [0, 1, 0, 1, 3, 1],
           [1, 0, 1, 0, 1, 2]]


def pentest(net):

    counter, pinged, downed = 0, {0}, {0}
    diag = [j[i] for i, j in enumerate(net) ]
    Nodes = [[j for j, column in enumerate(row) if column and i != j] for i, row in enumerate(net)] # All items which not 0 and not on diag
    while True:
        pinged.update(item for item in range(len(net)) if [node for node in Nodes[item] if node in downed ])
        for i in pinged:
            if diag[i] > 0:
                diag[i] -= 1      #Decrease node strength to 0
            else:
                diag[i] = 0
        downed.update(item for item, strnght in enumerate(diag) if strnght == 0) #update infested node lists
        counter += 1
        if len(downed) == len(net):
            return counter

print (pentest(example))


