import pygame
from constants import *

class Foundation:

    def __init__(self, x, y,type):
        self.cards = []
        self.x = x
        self.y = y
        self.type = type

    def set_cards_pos(self):
        for card in self.cards:
            card.set_pos((self.x, self.y))

    def show_last(self):
        if len(self.cards) > 0:
            self.cards[-1].showing = True

    def get_selected_cards(self, pos):
        self.cards = self.cards[0:]

    def add_cards(self, cards):
        self.cards.append(cards[0])
        self.set_cards_pos()

    def is_clicked(self, pos):
        if (pos[0] >= self.x and pos[0] <= self.x + CARD_WIDTH) and (pos[1] >= self.y and pos[1] <= self.y + CARD_HEIGHT + (SHOWING_HEIGHT*len(self.cards))) :
            return True
        return False

    def valid_move(self,cards):
        if len(self.cards) > 0:
            if cards[0].suit == self.cards[-1].suit and RANKS.index(cards[0].rank) == RANKS.index(self.cards[-1].rank) +1:
                return True
            return False
        else:
            if cards[0].rank == 'ace':
                return True
            return False

    
    