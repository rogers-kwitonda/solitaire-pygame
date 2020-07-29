from constants import *


class Pile:

    def __init__(self, cards, x, y, type):
        self.cards = cards
        self.type = type
        self.x = x
        self.y = y
        
        if type == 'tableau':
            self.fanned = True
            self.show_last()

        elif type == 'foundation':
            self.fanned = False
            self.show_last()

        elif type == 'hand':
            self.fanned = False
            

        elif type == 'waste':
            self.fanned = False
        

        self.set_cards_pos()


    def set_cards_pos(self):
        if self.fanned:
            if self.type == 'tableau':
                count = 0
                for card in self.cards:
                    card.set_pos((self.x, self.y + SHOWING_HEIGHT*count))
                    count += 1
                return
            else:
                count = 0
                for card in self.cards:
                    card.set_pos((self.x, self.y + SHOWING_WIDTH*count))
                    count += 1
                return

        for card in self.cards:
            card.set_pos((self.x, self.y))


    def is_clicked(self, pos):
        if (pos[0] >= self.x and pos[0] <= self.x + CARD_WIDTH) and (pos[1] >= self.y and pos[1] <= self.y + CARD_HEIGHT + (SHOWING_HEIGHT*len(self.cards))) :
            return True
        return False

    def show_last(self):
        if len(self.cards) > 0:
            self.cards[-1].showing = True

    def is_valid_move(self, cards):
        if self.type == 'tableau':
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
        elif self.type == 'foundation':
            print("Checking foundation")
            if len(cards) == 1:
                rank_of_top_card = cards[0].rank
                color_of_top_card = cards[0].color

                if len(self.cards) > 0:
                    color_of_last_card = self.cards[len(self.cards)-1].color
                    rank_of_last_card = self.cards[len(self.cards)-1].rank
                    print(rank_of_last_card, color_of_last_card, rank_of_top_card,  color_of_top_card)
                    if color_of_last_card == color_of_top_card and RANKS.index(rank_of_top_card) == RANKS.index(rank_of_last_card) + 1 :
                        return True
                    return False
                
                if cards[0].rank == 'ace':
                    return True
                return False

    def get_selected(self, pos):
        selected = []
        if self.type == 'tableau':
            if len(self.cards) > 0:
                # Check if its the last card in pile that is clicked
                if self.cards[-1].is_clicked(pos):
                    selected.append(self.cards.pop())
                    return selected
                # Get all cards clicked
                else:
                    index = 0
                    for card in self.cards:
                        if card.is_clicked_top(pos):
                            selected = self.cards[index:]
                            self.cards = self.cards[0:index]
                            break
                        index += 1
                    return selected
            return selected

        elif self.type == 'foundation':
            if len(self.cards) > 0:
                selected.append(self.cards.pop())
                return selected
            return selected

        elif self.type == 'hand':
            if len(self.cards) > 0:
                if self.cards[-1].is_clicked(pos):
                    selected.append(self.cards.pop())
                    return selected
                return selected
            return selected
        else:
            # Waste pile
            if len(self.cards) > 0:
                selected.append(self.cards.pop())
            return selected


    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)
        self.set_cards_pos()

