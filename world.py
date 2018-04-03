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
        self.targetRed3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde1.id)
        self.targetRed3.color = (240, 128, 128)
        self.targetRed4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde1.id)
        self.targetRed4.color = (240, 128, 128)
        self.targetRed5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde1.id)
        self.targetRed5.color = (240, 128, 128)

        self.targetGreen1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen1.color = (128, 240, 128)
        self.targetGreen2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen2.color = (128, 240, 128)
        self.targetGreen3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen3.color = (128, 240, 128)
        self.targetGreen4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen4.color = (128, 240, 128)
        self.targetGreen5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde2.id)
        self.targetGreen5.color = (128, 240, 128)

        self.targetBlue1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde3.id)
        self.targetBlue1.color = (128, 128, 240)
        self.targetBlue2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde3.id)
        self.targetBlue2.color = (128, 128, 240)
        self.targetBlue3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde3.id)
        self.targetBlue3.color = (128, 128, 240)
        self.targetBlue4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde3.id)
        self.targetBlue4.color = (128, 128, 240)
        self.targetBlue5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde3.id)
        self.targetBlue5.color = (128, 128, 240)

        self.targetYellow1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde4.id)
        self.targetYellow1.color = (240, 240, 128)
        self.targetYellow2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde4.id)
        self.targetYellow2.color = (240, 240, 128)
        self.targetYellow3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde4.id)
        self.targetYellow3.color = (240, 240, 128)
        self.targetYellow4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde4.id)
        self.targetYellow4.color = (240, 240, 128)
        self.targetYellow5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde4.id)
        self.targetYellow5.color = (240, 240, 128)

        self.targetPurple1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde5.id)
        self.targetPurple1.color = (240, 128, 240)
        self.targetPurple2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde5.id)
        self.targetPurple2.color = (240, 128, 240)
        self.targetPurple3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde5.id)
        self.targetPurple3.color = (240, 128, 240)
        self.targetPurple4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde5.id)
        self.targetPurple4.color = (240, 128, 240)
        self.targetPurple5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.clyde5.id)
        self.targetPurple5.color = (240, 128, 240)

        self.Targets = [self.targetRed1, self.targetRed2, self.targetRed3, self.targetRed4, self.targetRed5,
                        self.targetGreen1, self.targetGreen2, self.targetGreen3, self.targetGreen4, self.targetGreen5,
                        self.targetBlue1, self.targetBlue2, self.targetBlue3, self.targetBlue4, self.targetBlue5,
                        self.targetYellow1, self.targetYellow2, self.targetYellow3, self.targetYellow4, self.targetYellow5,
                        self.targetPurple1, self.targetPurple2, self.targetPurple3, self.targetPurple4, self.targetPurple5]

        #for target in self.Targets:
        #    print target.owner

    def update(self, time_passed, screen):
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
        if self.clyde1.targetsFound == 5 \
                or self.clyde2.targetsFound == 5 \
                or self.clyde3.targetsFound == 5 \
                or self.clyde4.targetsFound == 5 \
                or self.clyde5.targetsFound == 5:
            return True
