from typing import List
import random


class CardValue:
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"


class CardSuit:
    SPADE = "\u2664"
    CLUB = "\u2667"
    HEART = "\u2665"
    DIAMOND = "\u2666"


class Card:
    def __init__(self, card_value: CardValue, card_suit: CardSuit) -> None:
        self._value = card_value
        self._suit = card_suit

    def __str__(self) -> str:
        return self._suit + self._value

    def __eq__(self, __o: object) -> bool:
        return (self._value == __o.get_value()) and (self._suit == __o.get_suit())
    
    def __ne__(self, __o: object) -> bool:
        return (self._value != __o.get_value()) or (self._suit != __o.get_suit())
    
    def get_value(self) -> CardValue:
        return self._value

    def get_suit(self) -> CardSuit:
        return self._suit
        
        
class Deck:
    def __init__(self, random_init: bool = True) -> None:
        self._deck = [Card(getattr(CardValue, card_value), getattr(CardSuit, card_suit)) 
                      for card_value in dir(CardValue) if card_value.find("_") == -1
                      for card_suit in dir(CardSuit) if card_suit.find("_") == -1]
        self._length = len(self._deck)
        if (random_init):
            random.shuffle(self._deck)
    
    def __str__(self) -> str:
        string = "Number of Cards In Deck: " + str(self._length) + "\nOrder:\n"
        for i in range(self._length):
            string += str(self._deck[i]) + "\n"
        return string
    
    def get_deck_size(self) -> int:
        return self._length

    def draw_card(self) -> Card:
        if self._length > 0:
            self._length -= 1
            return self._deck.pop()
    
    def draw_hand(self, num_cards: int) -> List[Card]:
        if self._length >= num_cards:
            hand = []
            for i in range(num_cards):
                hand.append(self._deck.pop())
            return hand
