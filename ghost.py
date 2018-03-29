import pygame
from pygame.locals import *
from vectors import Vector2D
from constants import *
from entities import DynamicEntity
from random import randint


class Ghost(DynamicEntity):
    def __init__(self, node):
        DynamicEntity.__init__(self, node)
        self.color = (0, 0, 255)
        self.direction = RIGHT
        self.target = self.node.neighbors[self.direction]
        #self.poi = Vector2D()
        
    def update(self, dt):
        #print self.direction
        self.position += self.direction*self.speed*dt
        overshot = self.overshotTarget()
        if overshot:
            self.node = self.target
            if self.node.portalNode:
                self.node = self.node.portalNode
            self.position = self.node.position

            validDirections = self.getValidDirections()
            #index = self.getClosestNode(validDirections)
            index = randint(0, len(validDirections)-1)
            self.direction = validDirections[index]
            self.target = self.node.neighbors[self.direction]
        
    #def move(self, direction):
    #    pass

    #def getClosestNode(self, validDirections):
    #    distances = []
    #    for key in validDirections:
    #        diffVec = self.node.neighbors[key].position - self.poi
    #        distances.append(diffVec.magnitudeSquared())
    #    return distances.index(min(distances))

    def getValidDirections(self):
        validDirections = []
        for key in self.node.neighbors.keys():
            if self.node.neighbors[key] is not None:
                if not key == self.direction * -1:
                    validDirections.append(key)
        return validDirections
