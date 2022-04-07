import pygame

def run():
    pygame.init()
    sc = pygame.display.set_mode((900, 700))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

run()
