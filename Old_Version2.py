from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import myFunctions as mine
import time
#from matplotlib import animation
import matplotlib.animation as animation
# set up a figure twice as wide as it is tall
fig = plt.figure()

# set up the axes for the first plot
ax = fig.add_subplot(111, projection='3d')

#For simplicity, we are going to project onto the x/y plane, but other planes work
#defined by basis vectors as which is S matrix: 
# [[1], y
#  [0], x
#  [0]] z
basisProj1 = np.array([[0],[1],[0]])
# [[0], 
#  [1], 
#  [0]]
basisProj2 = np.array([[1],[0],[0]])

allBasis = np.concatenate((np.concatenate((basisProj1,
            np.array([[0],[0],[0]])), axis=1), basisProj2), axis=1)
#initial set up vertacies, which are two opposite faces of a parallelogram
#There are 5 verices because the way plotting works in matplotlib
square1 = np.array([[0, 0, 1, 1, 0], 
                    [0, 1, 1, 0, 0], 
                    [4, 4, 4, 4, 4]])

square2 = np.array([[0, 0, 1, 1, 0], 
                    [0, 1, 1, 0, 0], 
                    [6, 6, 6, 6, 6]])

theta = np.pi/4 # angle of rotation, but practiacally only controls direction
axis = np.array([[1],[1],[0]]) #axis of rotation, y x z
pauseLen = 0.001
rotationSpeed = 0.1
elev=50 #Vertical camera angle
azim=30 #HORIZONAL camera angle
azimSpeed = 1
animateMode = 1 #1 to animate, 0 for no animation
#SETTINGS COMPLETE
projectedSquare1 = np.array([[],[],[]])
projectedSquare2 = np.array([[],[],[]])
row, column = square1.shape
angle = 0 # starting angle

ax.view_init(elev, azim)
ax.set_xlim3d(-5, 5)
ax.set_ylim3d(-5, 5)
ax.set_zlim3d(-5, 5)
projectedSquare1 = np.array([[],[],[]])
projectedSquare2 = np.array([[],[],[]])
returnLines = []
square1, square2 = mine.rotation(0, square1, square2, axis)
for v in range(column):
    projectedSquare1 = np.concatenate((projectedSquare1, 
                                    mine.projectionOntoXY(square1[:,v], basisProj1, basisProj2)), axis=1)
    projectedSquare2 = np.concatenate((projectedSquare2, 
                                    mine.projectionOntoXY(square2[:,v], basisProj1, basisProj2)), axis=1)

Edge3d = mine.drawEdge2(square1,square2,'b', ax)
Edge2d = mine.drawEdge2(projectedSquare1,projectedSquare2,'b', ax)
returnLines = Edge3d + Edge2d

obj3D1, = ax.plot(square1[0,:], square1[1,:], square1[2,:], 'b')
obj3D2, = ax.plot(square2[0,:], square2[1,:], square2[2,:], 'b')
returnLines.extend([obj3D1, obj3D2])

obj2D1, = ax.plot(projectedSquare1[0,:], projectedSquare1[1,:], projectedSquare1[2,:], 'g')
obj2D2, = ax.plot(projectedSquare2[0,:], projectedSquare2[1,:], projectedSquare2[2,:], 'g')
returnLines.extend([obj2D1, obj2D2])


def UpdateReturn(newArray, oldArray, startingPoint):
    for x in range(len(newArray)):
        oldArray[startingPoint + x] = newArray[x]


def aniFunction(i):
    # Next 4 lines adjust the viewing angle/scaling
    Newsquare1, Newsquare2 = mine.rotation(rotationSpeed * i, square1, square2, axis)
    NewprojectedSquare1 = np.array([[],[],[]])
    NewprojectedSquare2 = np.array([[],[],[]])
    for v in range(column):
        NewprojectedSquare1 = np.concatenate((NewprojectedSquare1, 
                                        mine.projectionOntoXY(Newsquare1[:,v], basisProj1, basisProj2)), axis=1)
        NewprojectedSquare2 = np.concatenate((NewprojectedSquare2, 
                                        mine.projectionOntoXY(Newsquare2[:,v], basisProj1, basisProj2)), axis=1)
    newEdges3d = mine.drawEdge2(Newsquare1, Newsquare2, 'b', ax)
    UpdateReturn(newEdges3d, returnLines, 0)
    

    newEdges2d = mine.drawEdge2(NewprojectedSquare1, NewprojectedSquare2, 'g', ax)
    UpdateReturn(newEdges2d, returnLines, 4)

    newobj3D1, = ax.plot(Newsquare1[0,:], Newsquare1[1,:], Newsquare1[2,:], 'b')
    newobj3D2, = ax.plot(Newsquare2[0,:], Newsquare2[1,:], Newsquare2[2,:], 'b')

    returnLines[8] = newobj3D1
    returnLines[9] = newobj3D2

    newobj2D1, = ax.plot(NewprojectedSquare1[0,:], NewprojectedSquare1[1,:], NewprojectedSquare1[2,:], 'g')
    newobj2D2, = ax.plot(NewprojectedSquare2[0,:], NewprojectedSquare2[1,:], NewprojectedSquare2[2,:], 'g')

    
    returnLines[10] = newobj2D1
    returnLines[11] = newobj2D2


    return returnLines

ani = animation.FuncAnimation(fig, aniFunction, frames=200, interval=100, blit=True)

plt.show()