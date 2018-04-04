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
        self.agentRed = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.agentRed.color = (255, 0, 0)
        #print self.clyde1.id
        self.agentGreen = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.agentGreen.color = (0, 255, 0)
        #print self.clyde2.id
        self.agentBlue = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.agentBlue.color = (0, 0, 255)
        #print self.clyde3.id
        self.agentYellow = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.agentYellow.color = (255, 255, 0)
        #print self.clyde4.id
        self.agentPurple = Ghost(self.nodes.nodeList[randint(0, 2499)])
        self.agentPurple.color = (128, 0, 128)
        #print self.clyde5.id

        # initialize targets
        self.targetRed1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentRed.id)
        self.targetRed1.color = (240, 128, 128)
        self.targetRed2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentRed.id)
        self.targetRed2.color = (240, 128, 128)
        self.targetRed3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentRed.id)
        self.targetRed3.color = (240, 128, 128)
        self.targetRed4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentRed.id)
        self.targetRed4.color = (240, 128, 128)
        self.targetRed5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentRed.id)
        self.targetRed5.color = (240, 128, 128)

        self.targetGreen1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentGreen.id)
        self.targetGreen1.color = (128, 240, 128)
        self.targetGreen2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentGreen.id)
        self.targetGreen2.color = (128, 240, 128)
        self.targetGreen3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentGreen.id)
        self.targetGreen3.color = (128, 240, 128)
        self.targetGreen4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentGreen.id)
        self.targetGreen4.color = (128, 240, 128)
        self.targetGreen5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentGreen.id)
        self.targetGreen5.color = (128, 240, 128)

        self.targetBlue1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentBlue.id)
        self.targetBlue1.color = (128, 128, 240)
        self.targetBlue2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentBlue.id)
        self.targetBlue2.color = (128, 128, 240)
        self.targetBlue3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentBlue.id)
        self.targetBlue3.color = (128, 128, 240)
        self.targetBlue4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentBlue.id)
        self.targetBlue4.color = (128, 128, 240)
        self.targetBlue5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentBlue.id)
        self.targetBlue5.color = (128, 128, 240)

        self.targetYellow1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentYellow.id)
        self.targetYellow1.color = (240, 240, 128)
        self.targetYellow2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentYellow.id)
        self.targetYellow2.color = (240, 240, 128)
        self.targetYellow3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentYellow.id)
        self.targetYellow3.color = (240, 240, 128)
        self.targetYellow4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentYellow.id)
        self.targetYellow4.color = (240, 240, 128)
        self.targetYellow5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentYellow.id)
        self.targetYellow5.color = (240, 240, 128)

        self.targetPurple1 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentPurple.id)
        self.targetPurple1.color = (240, 128, 240)
        self.targetPurple2 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentPurple.id)
        self.targetPurple2.color = (240, 128, 240)
        self.targetPurple3 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentPurple.id)
        self.targetPurple3.color = (240, 128, 240)
        self.targetPurple4 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentPurple.id)
        self.targetPurple4.color = (240, 128, 240)
        self.targetPurple5 = PacMan(self.nodes.nodeList[randint(0, 2499)], self.agentPurple.id)
        self.targetPurple5.color = (240, 128, 240)

        self.Agents = [self.agentRed, self.agentGreen, self.agentBlue, self.agentYellow, self.agentPurple]

        self.Targets = [self.targetRed1, self.targetRed2, self.targetRed3, self.targetRed4, self.targetRed5,
                        self.targetGreen1, self.targetGreen2, self.targetGreen3, self.targetGreen4, self.targetGreen5,
                        self.targetBlue1, self.targetBlue2, self.targetBlue3, self.targetBlue4, self.targetBlue5,
                        self.targetYellow1, self.targetYellow2, self.targetYellow3, self.targetYellow4, self.targetYellow5,
                        self.targetPurple1, self.targetPurple2, self.targetPurple3, self.targetPurple4, self.targetPurple5]

        #for target in self.Targets:
        #    print target.owner

        self.checkList = []

        self.happinessList = []

    def update(self, time_passed, screen):
        self.checkTargetsAquired()

        if self.agentRed.happiness:
            self.happinessList.append(self.agentRed.happiness[-1])
        if self.agentGreen.happiness:
            self.happinessList.append(self.agentGreen.happiness[-1])
        if self.agentBlue.happiness:
            self.happinessList.append(self.agentBlue.happiness[-1])
        if self.agentYellow.happiness:
            self.happinessList.append(self.agentYellow.happiness[-1])
        if self.agentPurple.happiness:
            self.happinessList.append(self.agentPurple.happiness[-1])

        if self.happinessList:
            if self.happinessList.index(max(self.happinessList)) == 0:
                self.agentRed.isMostHappy = True
            else:
                self.agentRed.isMostHappy = False

            if self.happinessList.index(max(self.happinessList)) == 1:
                self.agentRed.isMostHappy = True
            else:
                self.agentRed.isMostHappy = False

            if self.happinessList.index(max(self.happinessList)) == 2:
                self.agentRed.isMostHappy = True
            else:
                self.agentRed.isMostHappy = False

            if self.happinessList.index(max(self.happinessList)) == 3:
                self.agentRed.isMostHappy = True
            else:
                self.agentRed.isMostHappy = False

            if self.happinessList.index(max(self.happinessList)) == 4:
                self.agentRed.isMostHappy = True
            else:
                self.agentRed.isMostHappy = False

        for target in self.Targets:
            if target.isInCheckList:
                if target not in self.checkList:
                    self.checkList.append(target)
                    #print self.checkList

            if target.isFound:
                if target in self.checkList:
                    self.checkList.remove(target)
                    #print self.checkList
                self.Targets.remove(target)
            #target.update()

        self.agentRed.update(time_passed, self.Targets, self.checkList)
        self.agentGreen.update(time_passed, self.Targets, self.checkList)
        self.agentBlue.update(time_passed, self.Targets, self.checkList)
        self.agentYellow.update(time_passed, self.Targets, self.checkList)
        self.agentPurple.update(time_passed, self.Targets, self.checkList)

        # render targets
        for target in self.Targets:
            target.render(screen)

        # render agents
        self.agentRed.render(screen)
        self.agentGreen.render(screen)
        self.agentBlue.render(screen)
        self.agentYellow.render(screen)
        self.agentPurple.render(screen)

    def returnNodes(self):
        return self.nodes

    def checkTargetsAquired(self):
        if self.agentRed.targetsFound == 5 \
                or self.agentGreen.targetsFound == 5 \
                or self.agentBlue.targetsFound == 5 \
                or self.agentYellow.targetsFound == 5 \
                or self.agentPurple.targetsFound == 5:
            return True
