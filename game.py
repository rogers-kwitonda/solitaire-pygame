import pygame
from os import listdir
from time import sleep
from constants import *


from deck import Deck

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.init()
pygame.display.set_caption("Solitaire")


def game():
    deck = Deck()
    deck.loadCards()
    deck.shuffle()
    deck.deal()

    selected_card = []
    selected_pile = None

    # Game Loop
    run = True

    while run:
        #Draw background
        win.fill((0,0,100))

        # Check for win
        if deck.check_win():
            run = False

        # Stock pile outline
        pygame.draw.rect(win, (0,255,0),(150,50,CARD_WIDTH, CARD_HEIGHT),1)

        # Draw foundation outlines
        pygame.draw.rect(win, (255,0,0),(500,50,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, (255,0,0),(650,50,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, (255,0,0),(800,50,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, (255,0,0),(950,50,CARD_WIDTH, CARD_HEIGHT),1)

        # Draw tableau outlines
        pygame.draw.rect(win, BLUE,(50,300,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, BLUE,(200,300,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, BLUE,(350,300,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, BLUE,(500,300,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, BLUE,(650,300,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, BLUE,(800,300,CARD_WIDTH, CARD_HEIGHT),1)
        pygame.draw.rect(win, BLUE,(950,300,CARD_WIDTH, CARD_HEIGHT),1)

        # Draw cards
        for pile in deck.piles:
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
                    deck.process_click(event.pos)
                    
            # 'MOUSEBUTTONUP' event
            if event.type == pygame.MOUSEBUTTONUP:
                pass

        pygame.display.update()





def start_graphic(window):
    spades = pygame.transform.scale(pygame.image.load('./cards/ace_of_spades.png'), (CARD_WIDTH, CARD_HEIGHT))
    clubs = pygame.transform.scale(pygame.image.load('./cards/ace_of_clubs.png'), (CARD_WIDTH, CARD_HEIGHT))
    diamonds = pygame.transform.scale(pygame.image.load('./cards/ace_of_diamonds.png'), (CARD_WIDTH, CARD_HEIGHT))
    hearts = pygame.transform.scale(pygame.image.load('./cards/ace_of_hearts.png'), (CARD_WIDTH, CARD_HEIGHT))

    window.blit(spades,(350,150))
    window.blit(diamonds,(500,150))
    window.blit(clubs,(650,150))
    window.blit(hearts,(800,150))

def start_screen():
    title_font = pygame.font.Font('freesansbold.ttf',96)
    
    title = title_font.render('Solitaire', True,(255,255,255))
    title_rect = title.get_rect()
    title_rect.center = (WIDTH//2, HEIGHT//2)

    instruction_font = pygame.font.Font('freesansbold.ttf',32)


    instruction = instruction_font.render('Place SPACE to start', True,RED)
    instruction_rect = instruction.get_rect()
    instruction_rect.center = (WIDTH//2, HEIGHT - 200)

    run = True
    while run:
        win.fill(GREEN)
        
        win.blit(title, title_rect)
        win.blit(instruction, instruction_rect)

        start_graphic(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # 'MOUSEBUTTONDOWN' event
            if event.type == pygame.KEYDOWN:
                # Check for left-click
                if event.key == pygame.K_SPACE:
                    game()                  

        pygame.display.update()





#start_screen()
game()