import pygame
from constants import *

class Card:

    def __init__(self, suit, rank, image):
        self.rank = rank
        self.suit = suit
        self.image = pygame.transform.scale(pygame.image.load('./cards/'+image), (CARD_WIDTH, CARD_HEIGHT))
        self.back = pygame.transform.scale(pygame.image.load('./cards/back.png'), (CARD_WIDTH, CARD_HEIGHT))
        self.showing = False
        self.x = 0
        self.y = 0

        if suit == 'spades' or suit == 'clubs':
            self.color = 'black'
        else:
            self.color = 'red'

    def __str__(self):
        return "{} of {}: {}".format(self.rank, self.suit, self.color)

    def is_clicked_top(self, pos):
        if (pos[0] >= self.x and pos[0] <= self.x + CARD_WIDTH) and (pos[1] >= self.y and pos[1] <= self.y + SHOWING_HEIGHT):
            return True
        return False
    
    def is_clicked(self, pos):
        if (pos[0] >= self.x and pos[0] <= self.x + CARD_WIDTH) and (pos[1] >= self.y and pos[1] <= self.y + CARD_HEIGHT):
            return True
        return False

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_image(self):
        if self.showing:
            return self.image
        return self.back