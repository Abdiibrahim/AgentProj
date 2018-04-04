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

    if world.checkTargetsAquired():
        print "\n"
        print "Targets Found:"
        print "Red   ", world.agentRed.targetsFound
        print "Green ", world.agentGreen.targetsFound
        print "Blue  ", world.agentBlue.targetsFound
        print "Yellow", world.agentYellow.targetsFound
        print "Purple", world.agentPurple.targetsFound
        print "Moves to collect all targets:"
        print "Red   ", world.agentRed.movesToComplete
        print "Green ", world.agentGreen.movesToComplete
        print "Blue  ", world.agentBlue.movesToComplete
        print "Yellow", world.agentYellow.movesToComplete
        print "Purple", world.agentPurple.movesToComplete
        print "Total Moves:"
        print "Red   ", world.agentRed.moves
        print "Green ", world.agentGreen.moves
        print "Blue  ", world.agentBlue.moves
        print "Yellow", world.agentYellow.moves
        print "Purple", world.agentPurple.moves
        exit()

    time_passed = pygame_clock.tick(30) / 1000.0

    screen.blit(background, (0, 0))
    world.nodes.render(screen)
    world.update(time_passed, screen)
    pygame.display.update()
