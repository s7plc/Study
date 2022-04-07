import pygame
import sys

def display():
    pygame.init()
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("try to survival")
    bg_color = (0, 0, 0)

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


while True:
    display()
    events()