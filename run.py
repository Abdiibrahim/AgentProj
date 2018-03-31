import pygame
from pygame.locals import *
from pacman import PacMan
from ghost import Ghost
from nodes import NodeGroup
from random import randint


gridUnit = 10
pygame.init()
SCREENSIZE = (102*gridUnit, 102*gridUnit)
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

nodes = NodeGroup(gridUnit, gridUnit)
nodes.createNodeListFromFile("map.txt")

print "Total nodes: ", len(nodes.nodeList)

#pacman = PacMan(nodes.nodeList[randint(0, 2499)])
ghost1 = Ghost(nodes.nodeList[randint(0, 2499)])
ghost1.color = (255, 0, 0)
ghost2 = Ghost(nodes.nodeList[randint(0, 2499)])
ghost2.color = (0, 255, 0)
ghost3 = Ghost(nodes.nodeList[randint(0, 2499)])
ghost3.color = (0, 0, 255)

while True:
    time_passed = clock.tick(30) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            print "Total Moves:"
            print "Ghost1: ", ghost1.moves
            print "Ghost2: ", ghost2.moves
            print "Ghost3: ", ghost3.moves
            exit()

    #pacman.update(time_passed)
    ghost1.update(time_passed)
    ghost2.update(time_passed)
    ghost3.update(time_passed)
    screen.blit(background, (0, 0))
    nodes.render(screen)
    #pacman.render(screen)
    ghost1.render(screen)
    ghost2.render(screen)
    ghost3.render(screen)
    pygame.display.update()
