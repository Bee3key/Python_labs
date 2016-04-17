__author__ = 'Bee3Key'


matrix = [[0, 1, 0, 1, 0, 1],
           [1, 8, 1, 0, 0, 0],
           [0, 1, 2, 0, 0, 1],
           [1, 0, 0, 1, 1, 0],
           [0, 0, 0, 1, 3, 1],
           [1, 0, 1, 0, 1, 2]]

def fff(rix):
    reached, injected = {0}, {0}
    security_levels = [row[i] for i, row in enumerate(matrix)]
    print(security_levels)
    connected = [[j for j, x in enumerate(row) if x and i != j] for i, row in enumerate(matrix)]
    print(connected)
    time = 0
    while True:
        print ("time", time)
        print ("security_level", security_levels)
        reached.update(x for x in range(len(matrix)) if [y for y in connected[x] if y in injected])
        print ("reached", reached)
        print ("len_reached", len(reached))
        # attack
        for i in reached:
            security_levels[i] -= 1 if security_levels[i] > 0 else 0
        injected.update(i for i, x in enumerate(security_levels) if x == 0)
        time += 1
        print ("injected", injected)
        print ("len_inj", len(injected))

        if len(injected) == len(matrix):
            return time


print(fff(matrix))
