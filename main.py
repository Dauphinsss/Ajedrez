import pygame
from gadgets import SCREEN_WIDTH, SCREEN_HEIGHT
from board import Board
from runner import game_run

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Checkers")
    board = Board()

    game_run(screen, board)

if __name__ == "__main__":
    main()