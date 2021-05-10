from game import Game
import pygame
g = Game()

while g.running:
    pygame.display.set_caption("SERPIENCOVID GAME")
    g.curr_menu.display_menu()
    g.game_loop()

