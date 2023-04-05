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

#WORKING STUFF
if (animateMode == 1):
    #FuncAnimation is too dificult and hard to understand, xd
    while(angle < theta):
        # Next 4 lines adjust the viewing angle/scaling
        ax.view_init(elev, azim)
        ax.set_xlim3d(-5, 5)
        ax.set_ylim3d(-5, 5)
        ax.set_zlim3d(-5, 5)
        projectedSquare1 = np.array([[],[],[]])
        projectedSquare2 = np.array([[],[],[]])
        square1, square2 = mine.rotation(angle, square1, square2, axis)
        for v in range(column):
            projectedSquare1 = np.concatenate((projectedSquare1, 
                                            mine.projectionOntoXY(square1[:,v], basisProj1, basisProj2)), axis=1)
            projectedSquare2 = np.concatenate((projectedSquare2, 
                                            mine.projectionOntoXY(square2[:,v], basisProj1, basisProj2)), axis=1)

        mine.drawEdge(square1, square2, 'b')
        plt.plot(square1[0,:], square1[1,:], square1[2,:], 'b')
        plt.plot(square2[0,:], square2[1,:], square2[2,:], 'b')
        mine.drawEdge(projectedSquare1, projectedSquare2, 'g')
        plt.plot(projectedSquare1[0,:], projectedSquare1[1,:], projectedSquare1[2,:], 'g')
        plt.plot(projectedSquare2[0,:], projectedSquare2[1,:], projectedSquare2[2,:], 'g')
        plt.plot(np.array([1,0,0]), np.array([0,0,0]), np.array([0,0,1]), 'r') #red axis of y and z
        plt.plot(allBasis[0,:], allBasis[1,:], allBasis[2,:], 'y')
        #next two lines analogous to "frame rate" and animation time
        plt.pause(pauseLen) 
        angle = theta * rotationSpeed
        plt.clf()
        ax = fig.add_subplot(111, projection='3d') 
        #^^keeps 3d setting from getting reset from clf()
        ax.set_xlim(-5,5)
        ax.set_ylim(-5,5)
        ax.set_zlim(-5,5)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        azim = azim + azimSpeed
else:
    square1, square2 = mine.rotation(angle, square1, square2, axis)
    for v in range(column):
        projectedSquare1 = np.concatenate((projectedSquare1, 
                                        mine.projectionOntoXY(square1[:,v], basisProj1, basisProj2)), axis=1)
        projectedSquare2 = np.concatenate((projectedSquare2, 
                                        mine.projectionOntoXY(square2[:,v], basisProj1, basisProj2)), axis=1)

    mine.drawEdge(square1, square2, 'b')
    plt.plot(square1[0,:], square1[1,:], square1[2,:], 'b')
    plt.plot(square2[0,:], square2[1,:], square2[2,:], 'b')
    mine.drawEdge(projectedSquare1, projectedSquare2, 'g')
    plt.plot(projectedSquare1[0,:], projectedSquare1[1,:], projectedSquare1[2,:], 'g')
    plt.plot(projectedSquare2[0,:], projectedSquare2[1,:], projectedSquare2[2,:], 'g')
    #plt.plot(np.array([1,0,0]), np.array([0,0,0]), np.array([0,0,1]), 'r') #red axis of y and z
    plt.plot(allBasis[0,:], allBasis[1,:], allBasis[2,:], 'y') # displays basis vectors
    #^^keeps 3d setting from getting reset from clf()
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_zlim(-5,5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

plt.show()