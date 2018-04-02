import pygame
from pygame.locals import *
from vectors import Vector2D
from constants import *
from entities import DynamicEntity
from random import randint


class Ghost(DynamicEntity):
    def __init__(self, node):
        DynamicEntity.__init__(self, node)
        # self.id = 1 make this update every time a Ghost object is instantiated
        self.color = (0, 0, 255)
        self.direction = RIGHT
        self.target = self.node.neighbors[self.direction]
        self.moves = 0
        self.poi = Vector2D()
        self.radiusSquared = (gridUnit * 22)**2

    def update(self, dt, pacman):
        #print self.direction
        self.position += self.direction*self.speed*dt
        overshot = self.overshotTarget()
        if overshot:
            self.node = self.target
            self.position = self.node.position

            validDirections = self.getValidDirections()

            distanceVector = pacman.position - self.position
            distanceSquared = distanceVector.magnitudeSquared()
            if (distanceSquared <= self.radiusSquared) and (distanceSquared != 0):

                # CHeck the targets associated agent, if it isn't this agents target dont go to it, return the position of the target and tell the other agents

                index = self.getClosestNode(validDirections)
                self.poi = pacman.position
                if distanceSquared == 0:
                    print self.moves
                    self.poi = Vector2D()
            else:
                index = randint(0, len(validDirections)-1)
            self.direction = validDirections[index]
            self.target = self.node.neighbors[self.direction]
            self.moves += 1
        
    #def move(self, direction):
    #    pass

    def getClosestNode(self, validDirections):
        distances = []
        for key in validDirections:
            diffVec = self.node.neighbors[key].position - self.poi
            distances.append(diffVec.magnitudeSquared())
        return distances.index(min(distances))

    def getValidDirections(self):
        validDirections = []
        for key in self.node.neighbors.keys():
            if self.node.neighbors[key] is not None:
                if not key == self.direction * -1:
                    validDirections.append(key)
        return validDirections

    #def getTargets(self):
    #    targets = []
