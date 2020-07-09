import pygame
from os import listdir
from time import sleep
from constants import *


from deck import Deck



win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.init()
pygame.display.set_caption("Solitaire")

deck = Deck()
deck.loadCards()
deck.shuffle()
deck.deal()




def removeCard(card):
    for pile in deck.piles:
        if card in pile.cards:
            pile.cards.remove(card)
# Game Loop
run = True
current_selection = None
previous_pile = None

while run:

    #Draw background
    win.fill((0,100,100))

    # Draw cards
    for pile in deck.piles:
        if pile.type == 'foundation':
            pygame.draw.rect(win,(0,0,255),[pile.x-5,pile.y-5,130,210])
        for card in pile.cards:
            win.blit(card.get_image(), (card.x, card.y))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # 'MOUSEBUTTONDOWN' event
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Check for left-click
            if event.button == 1:
                
                # Check if cards are currently selected
                if current_selection:
                    # Move cards
                    for pile in deck.piles:
                        if pile.is_clicked(event.pos):
                            if pile.valid_move(current_selection):
                                pile.add_cards(current_selection)
                                previous_pile.show_last()
                                current_selection = None
                                previous_pile = None
                                break
                            else:
                                previous_pile.restore_prev_state()
                                current_selection = None
                                previous_pile = None
                                break

                else:
                    # Select cards
                    for pile in deck.piles:
                        if pile.is_clicked(event.pos):
                            current_selection = pile.get_selected_cards(event.pos)
                            previous_pile = pile

        # 'MOUSEBUTTONUP' event
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    pygame.display.update()

pygame.quit()









