import pygame

def handle_events(board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True