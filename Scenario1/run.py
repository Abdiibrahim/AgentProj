import pygame
from pygame.locals import *
from constants import *
from world import World
import numpy as np


print "Starting Simulation: Scenario 1...\n"
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
        print "STATISTICS"
        print "=========="
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
        print "Agent Happiness:"
        print "Red   ", float(world.agentRed.targetsFound / (world.agentRed.moves + 1))
        print "Green ", float(world.agentGreen.targetsFound / (world.agentGreen.moves + 1))
        print "Blue  ", float(world.agentBlue.targetsFound / (world.agentBlue.moves + 1))
        print "Yellow", float(world.agentYellow.targetsFound / (world.agentYellow.moves + 1))
        print "Purple", float(world.agentPurple.targetsFound / (world.agentPurple.moves + 1))
        print "Max Happiness:"
        print "Red   ", np.max(world.agentRed.happiness)
        print "Green ", np.max(world.agentGreen.happiness)
        print "Blue  ", np.max(world.agentBlue.happiness)
        print "Yellow", np.max(world.agentYellow.happiness)
        print "Purple", np.max(world.agentPurple.happiness)
        print "Min Happiness:"
        print "Red   ", np.min(world.agentRed.happiness)
        print "Green ", np.min(world.agentGreen.happiness)
        print "Blue  ", np.min(world.agentBlue.happiness)
        print "Yellow", np.min(world.agentYellow.happiness)
        print "Purple", np.min(world.agentPurple.happiness)
        print "Average Happiness:"
        print "Red   ", np.mean(world.agentRed.happiness)
        print "Green ", np.mean(world.agentGreen.happiness)
        print "Blue  ", np.mean(world.agentBlue.happiness)
        print "Yellow", np.mean(world.agentYellow.happiness)
        print "Purple", np.mean(world.agentPurple.happiness)
        print "Standard Deviation of Happiness:"
        print "Red   ", np.std(world.agentRed.happiness)
        print "Green ", np.std(world.agentGreen.happiness)
        print "Blue  ", np.std(world.agentBlue.happiness)
        print "Yellow", np.std(world.agentYellow.happiness)
        print "Purple", np.std(world.agentPurple.happiness)
        print "Agent Competitiveness:"
        print "Red   ", ((float(world.agentRed.targetsFound / (world.agentRed.moves + 1))) - np.min(world.agentRed.happiness))/(np.max(world.agentRed.happiness) - np.min(world.agentRed.happiness))
        print "Green ", ((float(world.agentGreen.targetsFound / (world.agentGreen.moves + 1))) - np.min(world.agentGreen.happiness))/(np.max(world.agentGreen.happiness) - np.min(world.agentGreen.happiness))
        print "Blue  ", ((float(world.agentBlue.targetsFound / (world.agentBlue.moves + 1))) - np.min(world.agentBlue.happiness))/(np.max(world.agentBlue.happiness) - np.min(world.agentBlue.happiness))
        print "Yellow", ((float(world.agentYellow.targetsFound / (world.agentYellow.moves + 1))) - np.min(world.agentYellow.happiness))/(np.max(world.agentYellow.happiness) - np.min(world.agentYellow.happiness))
        print "Purple", ((float(world.agentPurple.targetsFound / (world.agentPurple.moves + 1))) - np.min(world.agentPurple.happiness))/(np.max(world.agentPurple.happiness) - np.min(world.agentPurple.happiness))
        print "\n================="
        print "END OF SIMULATION"
        exit()

    time_passed = pygame_clock.tick(30) / 1000.0

    screen.blit(background, (0, 0))
    world.nodes.render(screen)
    world.update(time_passed, screen)
    pygame.display.update()
