import pygame
from constants import *

class Tableau:

    def __init__(self, cards, x, y,type):
        self.cards = cards
        self.type = type
        self.x = x
        self.y = y
        self.prev_state = None

        self.set_cards_pos()
        self.show_last()

    def set_cards_pos(self):
        count = 1
        for card in self.cards:
            card.set_pos((self.x, self.y + SHOWING_HEIGHT*count))
            count += 1
            
    def show_last(self):
        if len(self.cards) > 0:
            self.cards[-1].showing = True

    def get_selected_cards(self, pos):
        for card in self.cards:
            if card.is_clicked(pos) and card.showing:
                current_index = self.cards.index(card)
                selected = self.cards[current_index:]

                self.prev_state = self.cards
                self.cards = self.cards[:current_index]
                return selected

    def add_cards(self, cards):
        self.cards += cards
        self.show_last()
        self.set_cards_pos()

    def restore_prev_state(self):
        self.cards = self.prev_state
        self.prev_state = None
        
    def valid_move(self,cards):

        
        rank_of_top_card = cards[0].rank
        color_of_top_card = cards[0].color

        if len(self.cards) > 0:
            color_of_last_card = self.cards[len(self.cards)-1].color
            rank_of_last_card = self.cards[len(self.cards)-1].rank
            print(rank_of_last_card, rank_of_top_card, color_of_last_card, color_of_top_card)
            if color_of_last_card != color_of_top_card and RANKS.index(rank_of_top_card) == RANKS.index(rank_of_last_card) -1 :
                return True
            return False
        
        if cards[0].rank == 'king':
            return True
        return False

    def is_clicked(self, pos):
        if (pos[0] >= self.x and pos[0] <= self.x + CARD_WIDTH) and (pos[1] >= self.y and pos[1] <= self.y + CARD_HEIGHT + (SHOWING_HEIGHT*len(self.cards))) :
            return True
        return False

    
    