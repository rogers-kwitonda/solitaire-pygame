import random

import pygame
from os import listdir
from card import Card
from pile import Pile
from constants import *



class Deck:

    def __init__(self):
        self.deck = []
        self.piles = []
        self.selected = False
        self.selected_cards = []
        self.from_pile = None

    def loadCards(self):
        for suit in SUITS:
            for rank in RANKS:
                image_name = "{}_of_{}.png".format(rank,suit)
                card = Card(suit, rank, image_name)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
        random.shuffle(self.deck)      
    
    def deal(self):
        # Create and load cards into bottom piles
        self.piles.append(Pile([self.deck[0]], 50,300,'tableau'))
        self.piles.append(Pile(self.deck[1:3], 200,300,'tableau'))
        self.piles.append(Pile(self.deck[3:6], 350,300,'tableau'))
        self.piles.append(Pile(self.deck[6:10], 500,300,'tableau'))
        self.piles.append(Pile(self.deck[10:15], 650,300,'tableau'))
        self.piles.append(Pile(self.deck[15:21], 800,300,'tableau'))
        self.piles.append(Pile(self.deck[21:28], 950,300,'tableau'))

        # Create top piles
        self.piles.append(Pile([],500, 50, 'foundation'))
        self.piles.append(Pile([],650, 50, 'foundation'))
        self.piles.append(Pile([],800, 50, 'foundation'))
        self.piles.append(Pile([],950, 50, 'foundation'))

        # Load remaining cards into "hand"
        self.piles.append(Pile(self.deck[28:], 50,50, 'hand'))
        self.piles.append(Pile([], 150,50, 'waste'))

    def check_win(self):
        for pile in self.piles:
            if pile.type == 'foundation' and len(pile.cards) < 13:
                return False
        return True

    def process_click(self, pos):
        if not self.selected:
            # Player selects cards
            for pile in self.piles:
                if pile.is_clicked(pos):
                    if pile.type == 'tableau' or pile.type == 'foundation':
                        selected = pile.get_selected(pos)
                        if len(selected) > 0:
                            self.selected = True
                            self.from_pile = pile
                            self.selected_cards = selected
                            break
                    elif pile.type == 'waste':
                        selected = pile.get_selected(pos)
                        if len(selected) > 0:
                            self.selected = True
                            self.from_pile = pile
                            self.selected_cards = selected
                            break
                    elif pile.type == 'hand':
                        if len(pile.cards) > 0:
                            selected = pile.get_selected(pos)
                            for stack in self.piles:
                                if stack.type == 'waste':
                                    if len(selected) > 0:
                                        selected[0].showing = True
                                        stack.add_cards(selected)
                                        break
                        else:
                            for stack in self.piles:
                                if stack.type == 'waste':
                                    pile.cards = stack.cards
                                    stack.cards = []
                                    pile.set_cards_pos()
                                    print('Hand cards: ',pile.cards)
                                    print('Waste cards: ',stack.cards)
                                    for card in pile.cards:
                                        card.showing = False


        else:

            # Player moves card(s) to destination pile
            for pile in self.piles:
                if pile.is_clicked(pos):
                    if pile.type == 'tableau' or pile.type == 'foundation':
                        if pile.is_valid_move(self.selected_cards):
                            pile.add_cards(self.selected_cards)
                            self.from_pile.show_last()
                            self.selected_cards = []
                            self.selected = False
                            self.from_pile = None
                            

                        else:
                            self.from_pile.add_cards(self.selected_cards)
                            self.selected_cards = []
                            self.selected = False
                            self.from_pile = None
                        break
                



    