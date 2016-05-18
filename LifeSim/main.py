__author__ = 'Bee3Key'

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

LIVE = 255
DEAD = 0

game = [LIVE, DEAD]

def randField(d):
    return np.random.choice(game, d*d, p=[0.2, 0.8]).reshape(d, d)

def randShape(i, j, Sd, field):
    """
    Create s random shape with metric Sd and put it on the field
    """

    Shape =  np.random.choice([0, 255], Sd*Sd, p=[0.7, 0.3]).reshape(Sd, Sd)

    field[i:i+Sd, j:j+Sd] = Shape

def Glider(i, j, field):

    """
    Create a glider shape and put it on the field
    """
    glider = np.array([[0,0,255],
                       [255,0,255],
                       [0,255,255]])
    field[i:i+3, j:j+3] = glider

def update(frameNum, img, field, d):
    newField = field.copy()
    for i in range(d):
        for j in range(d):
            neighbors = int((field[i, (j-1)%d] + field[i, (j+1)%d] +
                         field[(i-1)%d, j] + field[(i+1)%d, j] +
                         field[(i-1)%d, (j-1)%d] + field[(i-1)%d, (j+1)%d] +
                         field[(i+1)%d, (j-1)%d] + field[(i+1)%d, (j+1)%d])/255)
            if field[i,j] == LIVE:
                if (neighbors <2) or (neighbors > 3):
                    newField[i,j] = DEAD
            if neighbors == 3:
                newField[i,j] = LIVE
    img.set_data(newField)
    field[:] = newField[:]
    return img




def main():

    argument = argparse.ArgumentParser(description="Lynn Conway's Game of Life Simulation")

    argument.add_argument('--field-metric', dest='d', required=False)
    argument.add_argument('--movi', dest='mov_file', required=False)
    argument.add_argument('--freq', dest='frequency', required=False)
    argument.add_argument('--glider', action='store_true', required=False)

    args = argument.parse_args()

    d = 100 #Metrika
    if args.d and int(args.d) > 10:
        d = int(args.d)

    Frequency = 45
    if args.frequency:
        Frequency = int(args.frequency)

    field = np.array([])

    if args.glider:
        field = np.zeros(d*d).reshape(d,d)
        Glider(1,1,field)
    else:
        field = randField(d)

    fig, ax = plt.subplots()
    img = ax.imshow(field, interpolation='nearest')
    ani = anime.FuncAnimation(fig, update, fargs=(img, field, d,),
                              frames=10,
                              interval=Frequency,
                              save_count=50
                              )
    if args.mov_file:
        ani.save(args.mov_file, fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()

if __name__ == '__main__':
    main()





