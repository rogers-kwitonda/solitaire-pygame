import pygame
from constants import *

class Hand:

    def __init__(self, cards, x, y,type):
        self.cards = cards
        self.type = "hand"
        self.x = x
        self.y = y

        self.set_cards_pos()

    def set_cards_pos(self):
        for card in self.cards:
            card.set_pos((self.x, self.y))
            
    def show_last(self):
        if len(self.cards) > 0:
            self.cards[-1].showing = True

    def get_selected_cards(self, pos):
        for card in self.cards:
            if card.is_clicked(pos) and card.showing:
                current_index = self.cards.index(card)
                selected = self.cards[current_index:]
                self.cards = self.cards[:current_index]
                self.show_last()
                return selected

    def add_cards(self, cards):
        self.cards += cards
        self.show_last()
        self.set_cards_pos()

    def is_clicked(self, pos):
        if (pos[0] >= self.x and pos[0] <= self.x + CARD_WIDTH) and (pos[1] >= self.y and pos[1] <= self.y + CARD_HEIGHT + (SHOWING_HEIGHT*len(self.cards))) :
            return True
        return False

    def valid_move(self,cards):
        rank_of_last_card = self.cards[len(self.cards)-1].rank
        rank_of_top_card = cards[0].rank
        color_of_last_card = self.cards[len(self.cards)-1].color
        color_of_top_card = cards[0].color

        if color_of_last_card != color_of_top_card and RANKS.index(rank_of_top_card) == RANKS.index(rank_of_last_card) -1 :
            return True
        return False

    
    