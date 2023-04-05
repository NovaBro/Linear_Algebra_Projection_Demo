import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def findOrthoNormal(vector1, vector2):
    unit1 = vector1 / np.sqrt(np.vdot(vector1,vector1))
    unit2 = ((vector2 - np.vdot(vector2,unit1) * unit1))
    unit2 = unit2/np.sqrt(np.vdot(unit2,unit2))
    return unit1, unit2

def projectionOntoXY(vector, basisProj1, basisProj2):
    basisVector1 = basisProj1 # BASIS VECTOR PLANE
    basisVector2 = basisProj2 # BASIS VECTOR PLANE
    unitVec1, unitVec2 = findOrthoNormal(basisVector1, basisVector2)
    vector = np.expand_dims(vector, axis=1)
    projection = np.vdot(unitVec1, vector) * unitVec1 + np.vdot(unitVec2, vector) * unitVec2
    return projection

def drawEdge(projections1, projections2, color):
    for c in range(4):
        plt.plot(np.array([projections1[0,c], projections2[0,c]]), 
                 np.array([projections1[1,c], projections2[1,c]]), 
                 np.array([projections1[2,c], projections2[2,c]]), color)
        
def drawEdge2(projections1, projections2, color, ax):
    returnArray = []
    for c in range(4):
        line = ax.plot(np.array([projections1[0,c], projections2[0,c]]), 
                 np.array([projections1[1,c], projections2[1,c]]), 
                 np.array([projections1[2,c], projections2[2,c]]), color)[0]
        returnArray.append(line)
    return returnArray

def drawEdge3(projections1, projections2, c):
    returnArray = np.array([[projections1[0,c], projections2[0,c]],
                            [projections1[1,c], projections2[1,c]],
                            [projections1[2,c], projections2[2,c]]])
    return returnArray

def rotation(angle, square1, square2, axis):
    unitAxis = axis / np.sqrt(axis[0,0]**2 + axis[1,0]**2 + axis[2,0]**2)
    newSquare1 = np.array([[],[],[]])
    newSquare2 = np.array([[],[],[]])
    for v in range(4):
        vector = np.expand_dims(square1[:,v], axis=1)
        #https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
        rotationVec = (vector * np.cos(angle) + np.cross(unitAxis, vector, axis=0) * 
                       np.sin(angle) + unitAxis * (np.vdot(unitAxis,vector)) * 
                       (1 - np.cos(angle)))
        newSquare1 = np.concatenate((newSquare1, rotationVec), axis=1)
   
    for v in range(4):
        vector = np.expand_dims(square2[:,v], axis=1)
        rotationVec = (vector * np.cos(angle) + np.cross(unitAxis, vector, axis=0) * 
                        np.sin(angle) + unitAxis * (np.vdot(unitAxis, vector)) * 
                        (1 - np.cos(angle))) 
        newSquare2 = np.concatenate((newSquare2, rotationVec), axis=1)

    newSquare1 = np.concatenate((newSquare1, np.expand_dims(newSquare1[:,0],axis=1)), axis=1)
    newSquare2 = np.concatenate((newSquare2, np.expand_dims(newSquare2[:,0],axis=1)), axis=1)

    return newSquare1, newSquare2


def rotation2(angle, square1, square2, axis):
    unitAxis = axis / np.sqrt(axis[0,0]**2 + axis[1,0]**2 + axis[2,0]**2)
    newSquare1 = np.array([[],[],[]])
    newSquare2 = np.array([[],[],[]])
    for v in range(4):
        vector = np.expand_dims(square1[:,v], axis=1)
        #https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula
        rotationVec = (vector * np.cos(angle) + np.cross(unitAxis, vector, axis=0) * 
                       np.sin(angle) + unitAxis * (np.vdot(unitAxis,vector)) * 
                       (1 - np.cos(angle)))
        newSquare1 = np.concatenate((newSquare1, rotationVec), axis=1)
   
    for v in range(4):
        vector = np.expand_dims(square2[:,v], axis=1)
        rotationVec = (vector * np.cos(angle) + np.cross(unitAxis, vector, axis=0) * 
                        np.sin(angle) + unitAxis * (np.vdot(unitAxis, vector)) * 
                        (1 - np.cos(angle))) 
        newSquare2 = np.concatenate((newSquare2, rotationVec), axis=1)

    newSquare1 = np.concatenate((newSquare1, np.expand_dims(newSquare1[:,0],axis=1)), axis=1)
    newSquare2 = np.concatenate((newSquare2, np.expand_dims(newSquare2[:,0],axis=1)), axis=1)

    return 0
