import random

import pygame
from os import listdir
from card import Card
from tableau import Tableau
from foundation import Foundation
from hand import Hand
from constants import *



class Deck:

    def __init__(self):
        self.deck = []
        self.piles = []

    def loadCards(self):
        for suit in SUITS:
            for rank in RANKS:
                image_name = "{}_of_{}.png".format(rank,suit)
                card = Card(suit, rank, image_name)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def clicked(self):
         pass       
    
    def deal(self):
        # Create and load cards into bottom piles
        self.piles.append(Tableau([self.deck[0]], 50,300,'tableau'))
        self.piles.append(Tableau(self.deck[1:3], 200,300,'tableau'))
        self.piles.append(Tableau(self.deck[3:6], 350,300,'tableau'))
        self.piles.append(Tableau(self.deck[6:10], 500,300,'tableau'))
        self.piles.append(Tableau(self.deck[10:15], 650,300,'tableau'))
        self.piles.append(Tableau(self.deck[15:21], 800,300,'tableau'))
        self.piles.append(Tableau(self.deck[21:28], 950,300,'tableau'))

        # Create top piles
        self.piles.append(Foundation(500, 50, 'foundation'))
        self.piles.append(Foundation(650, 50, 'foundation'))
        self.piles.append(Foundation(800, 50, 'foundation'))
        self.piles.append(Foundation(950, 50, 'foundation'))

        # Load remaining cards into "hand"
        self.piles.append(Hand(self.deck[28:], 50,50, 'hand'))



    