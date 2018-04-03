import pygame
from pygame.locals import *
from constants import *
from world import World


print "Starting Simulation...\n"
pygame.init()

SCREENSIZE = (102*gridUnit, 102*gridUnit)
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

world = World()
world.returnNodes()
pygame_clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    if world.targetsAquired():
        print "\n"
        print "Targets Found:"
        print "Red   ", world.clyde1.targetsFound
        print "Green ", world.clyde2.targetsFound
        print "Blue  ", world.clyde3.targetsFound
        print "Yellow", world.clyde4.targetsFound
        print "Purple", world.clyde5.targetsFound
        print "Total Moves:"
        print "Red   ", world.clyde1.moves
        print "Green ", world.clyde2.moves
        print "Blue  ", world.clyde3.moves
        print "Yellow", world.clyde4.moves
        print "Purple", world.clyde5.moves
        exit()

    time_passed = pygame_clock.tick(30) / 1000.0

    screen.blit(background, (0, 0))
    world.nodes.render(screen)
    world.update(time_passed, screen)
    pygame.display.update()
