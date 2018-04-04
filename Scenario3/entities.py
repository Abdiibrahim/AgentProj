import pygame
from constants import *
from vectors import Vector2D


class DynamicEntity(object):
    def __init__(self, node):
        self.node = node
        self.nextNode = node
        self.speed = 200
        self.setPosition()
        self.color = (255, 255, 255)
        
    def setPosition(self):
        self.position = Vector2D(self.node.position.x, self.node.position.y)

    def getNextTarget(self, direction):
        '''Get the next target as specified by the direction'''
        key = direction
        if self.node.neighbors[key] is not None:
            self.nextNode = self.node.neighbors[key]
        else:
            self.restOnNode()

    def overshotTarget(self):
        '''Returns True if moved passed target, False otherwise'''
        vec1 = self.nextNode.position - self.node.position
        vec2 = self.position - self.node.position
        nodeToTarget = vec1.magnitudeSquared()
        nodeToSelf = vec2.magnitudeSquared()
        return nodeToSelf > nodeToTarget

    def restOnNode(self):
        '''Rest on self.node'''
        self.setPosition()
        self.direction = STOP
        
    def render(self, screen):
        px = int(self.position.x)
        py = int(self.position.y)
        pygame.draw.circle(screen, self.color, (px, py), 10)
