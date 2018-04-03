from pacman import PacMan
from ghost import Ghost
from random import randint
from nodes import NodeGroup
from constants import *


class World(object):
    def __init__(self):
        self.nodes = NodeGroup(gridUnit, gridUnit)
        self.nodes.createNodeListFromFile("map.txt")

        # initialize agents
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

        # initialize targets
        self.targetRed1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde1.id)
        self.targetRed1.color = (240, 128, 128)
        self.targetRed2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde1.id)
        self.targetRed2.color = (240, 128, 128)
        self.targetGreen1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen1.color = (128, 240, 128)
        self.targetGreen2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen2.color = (128, 240, 128)

        self.Targets = [self.targetRed1, self.targetRed2, self.targetGreen1, self.targetGreen2]
        for target in self.Targets:
            print target.owner

    def update(self, time_passed, screen):
        if self.clyde1.targetsFound == 2 or self.clyde2.targetsFound == 2:
            self.targetsAquired()

        for target in self.Targets:
            if target.isFound:
                self.Targets.remove(target)
            target.update(time_passed)
        self.clyde1.update(time_passed, self.Targets)
        self.clyde2.update(time_passed, self.Targets)
        self.clyde3.update(time_passed, self.Targets)
        self.clyde4.update(time_passed, self.Targets)
        self.clyde5.update(time_passed, self.Targets)

        for target in self.Targets:
            target.render(screen)
        self.clyde1.render(screen)
        self.clyde2.render(screen)
        self.clyde3.render(screen)
        self.clyde4.render(screen)
        self.clyde5.render(screen)

    def returnNodes(self):
        return self.nodes

    def targetsAquired(self):
        print "\n"
        print "Targets Found:"
        print "Red  ", self.clyde1.targetsFound
        print "Green", self.clyde2.targetsFound
        exit()
