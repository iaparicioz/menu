import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 150, 100)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 60, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        #posiciones donde colocamos cada mensaje
        self.startx, self.starty = self.mid_w, self.mid_h - 150
        self.rankingx, self.rankingy = self.mid_w, self.mid_h - 80
        self.creditsx, self.creditsy = self.mid_w, self.mid_h - 10
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.GREEN)
            #tamaño de letras y posicion.
            self.game.draw_text('Main Menu', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -300)
            self.game.draw_text("Start Game", 70, self.startx, self.starty)
            self.game.draw_text("Ranking", 70, self.rankingx, self.rankingy)
            self.game.draw_text("Credits", 70, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            #para movernos por el main menu.
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.rankingx + self.offset, self.rankingy)
                self.state = 'Ranking'
            elif self.state == 'Ranking':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Ranking':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.rankingx + self.offset, self.rankingy)
                self.state = 'Ranking'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Ranking':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.GREEN)
            self.game.draw_text('RANKING', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.blit_screen()

    def check_input(self):
       if self.game.START_KEY:
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.GREEN)
            self.game.draw_text('Credits', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 300)
            self.game.draw_text('HECHO POR Ivonne Aparicio :)', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 70)
            self.game.draw_text('¡Gracias por jugar!', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()