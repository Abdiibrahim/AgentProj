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
        self.targetsFound = 0

        self.poi = Vector2D()
        self.radiusSquared = (gridUnit * 22)**2

    def update(self, dt, targetList):
        #print self.direction
        self.position += self.direction*self.speed*dt
        overshot = self.overshotTarget()
        if overshot:
            self.node = self.nextNode
            self.position = self.node.position

            validDirections = self.getValidDirections()

            dummylist = []
            for targ in targetList:
                targ.distanceVector = targ.position - self.position
                targ.distanceSquared = targ.distanceVector.magnitudeSquared()
                dummylist.append(targ.distanceSquared)

            closestTargetIndex = dummylist.index(min(dummylist))
            closestTarget = targetList[closestTargetIndex]

            if closestTarget.distanceSquared < self.radiusSquared:
                index = self.getClosestNode(validDirections)
                # Check the targets associated agent, if it isn't this agents target dont go to it, return the position of the target and tell the other agents
                if self.id == closestTarget.owner:
                    self.poi = closestTarget.position
                    if self.position == closestTarget.position:
                        self.setFound(targetList[closestTargetIndex])
                        index = randint(0, len(validDirections) - 1)
                    # Remove target from target list
                if self.id != closestTarget.owner:
                    self.alertOwner()
            else:
                index = randint(0, len(validDirections)-1)
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
            print self.moves

    def alertOwner(self):
        print "Alerting owner"
