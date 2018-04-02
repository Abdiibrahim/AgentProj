import pygame
from pygame.locals import *
from nodes import NodeGroup
from constants import *
from world import World


pygame.init()
SCREENSIZE = (102*gridUnit, 102*gridUnit)
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

nodes = NodeGroup(gridUnit, gridUnit)
nodes.createNodeListFromFile("map.txt")

world = World(pygame)
pygame_clock = pygame.time.Clock()

print "Total nodes:", len(nodes.nodeList)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    time_passed = pygame_clock.tick(30) / 1000.0

    screen.blit(background, (0, 0))
    nodes.render(screen)
    world.update(time_passed, screen)
    pygame.display.update()
