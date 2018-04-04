from constants import *
from entities import DynamicEntity
from random import randint


class Ghost(DynamicEntity):
    id_count = 1

    def __init__(self, node):
        DynamicEntity.__init__(self, node)
        self.id = Ghost.id_count
        Ghost.id_count += 1

        self.color = (0, 0, 255)
        self.direction = RIGHT
        self.nextNode = self.node.neighbors[self.direction]

        self.moves = 0
        self.movesToComplete = None
        self.targetsFound = 0

        self.poi = Vector2D()
        self.radiusSquared = (gridUnit * 22)**2

        self.closestCheck = None

    def update(self, dt, targetList, checkList):
        #print self.direction
        self.position += self.direction*self.speed*dt
        overshot = self.overshotTarget()
        if overshot:
            self.node = self.nextNode
            self.position = self.node.position

            validDirections = self.getValidDirections()
            self.ownerCheckList = []
            dummyCheckList = []
            dummyTargetList = []

            for check in checkList:
                if check.owner == self.id:
                    self.ownerCheckList.append(check)
            if self.ownerCheckList:
                for check in self.ownerCheckList:
                    check.distanceVector = check.position - self.position
                    check.distanceSquared = check.distanceVector.magnitudeSquared()
                    dummyCheckList.append(check.distanceSquared)
                closestCheckIndex = dummyCheckList.index(min(dummyCheckList))
                self.closestCheck = self.ownerCheckList[closestCheckIndex]

            for target in targetList:
                target.distanceVector = target.position - self.position
                target.distanceSquared = target.distanceVector.magnitudeSquared()
                dummyTargetList.append(target.distanceSquared)
            closestTargetIndex = dummyTargetList.index(min(dummyTargetList))
            closestTarget = targetList[closestTargetIndex]

            if self.ownerCheckList:
                index = self.getClosestNode(validDirections)
                self.poi = self.closestCheck.position
                if self.position == self.closestCheck.position:
                    self.setFound(self.closestCheck)
            elif closestTarget.distanceSquared <= self.radiusSquared:
                index = self.getClosestNode(validDirections)
                if self.id == closestTarget.owner:
                    self.poi = closestTarget.position
                    if self.position == closestTarget.position:
                        if not closestTarget.isFound:
                            self.setFound(closestTarget)
                        index = randint(0, len(validDirections) - 1)
                else:
                    if not targetList[closestTargetIndex].isInCheckList:
                        self.setIsInCheckList(targetList[closestTargetIndex])
                    index = randint(0, len(validDirections) - 1)
            else:
                index = randint(0, len(validDirections) - 1)
            self.direction = validDirections[index]
            self.nextNode = self.node.neighbors[self.direction]
            self.moves += 1

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

    def setFound(self, target):
        target.isFound = True
        self.targetsFound += 1
        if self.targetsFound == 5:
            self.movesToComplete = self.moves
        #print self.moves
        #print self.movesToComplete

    def setIsInCheckList(self, target):
        target.isInCheckList = True
