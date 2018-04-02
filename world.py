from pacman import PacMan
from ghost import Ghost
from random import randint
from nodes import NodeGroup
from constants import *


class World(object):
    def __init__(self):

        self.nodes = NodeGroup(gridUnit, gridUnit)
        self.nodes.createNodeListFromFile("map.txt")

        self.clyde1 = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.clyde1.color = (255, 0, 0)
        #print self.clyde1.id
        self.clyde2 = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.clyde2.color = (0, 255, 0)
        #print self.clyde2.id
        self.clyde3 = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.clyde3.color = (0, 0, 255)
        #print self.clyde3.id
        self.clyde4 = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.clyde4.color = (255, 255, 0)
        #print self.clyde4.id
        self.clyde5 = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.clyde5.color = (128, 0, 128)
        #print self.clyde5.id

        self.pacman = PacMan(self.nodes.nodeList[1275], self.clyde1.id)

    def update(self, time_passed, screen):

        self.pacman.update(time_passed)
        self.clyde1.update(time_passed, self.pacman)
        self.clyde2.update(time_passed, self.pacman)
        self.clyde3.update(time_passed, self.pacman)
        self.clyde4.update(time_passed, self.pacman)
        self.clyde5.update(time_passed, self.pacman)

        self.pacman.render(screen)
        self.clyde1.render(screen)
        self.clyde2.render(screen)
        self.clyde3.render(screen)
        self.clyde4.render(screen)
        self.clyde5.render(screen)
