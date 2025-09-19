import random
import pygame

class Button():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = pos

    def clicked (self.pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0]> self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
            return False
class RpsGame():
    def __init__(self):
        pygame.init()
                
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")
        self.bg = pygame.image.load("C:\Users\shyle\Downloads\background.jpg")
        self.r_btn = pygame.image.load("C:\Users\shyle\Downloads\r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("C:\Users\shyle\Downloads\p_button.png").convert_alpha()
        self.s_btn =pygame.image.load("C:\Users\shyle\Downloads\s_button.png").covert_alpha()

        self.choose_rock = pygame.image.load("C:\Users\shyle\Downloads\rock.png")