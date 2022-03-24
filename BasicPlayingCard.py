"""
Ideal Abstraction Class for defining basic card objects
for arbitrary card games. Class comes pre-initialized
with traditional card decks (such as standard 52-cards, tarots, etc)
but also has the option for defining custom cards

Features of Basic Card Include
- Card Value
- Card Rank
- Card Image
- Card Name
- Card Value Ranking (Comparing with Other Cards)
- Card Suit Ranking
- Card Suit vs Value Ranking (Priority)

What this class abstraction does NOT do:
- Advanced rulesets that are specific to paricular gameplay:
  i.e. Ace can be valued as both 1 and 14 in a standard 52-card deck
"""

"""
Documentation
-------------
- How to create preset Cards
- How to create custom Cards
"""

from typing import Dict, List, Tuple
import re
import random

PRIORITY_VALUE = "PRI_VALU"
PRIORITY_RANK = "PRI_RANK"
PRIORITY_NEUTRAL = "PRI_NEUT"

SUBSTITUTION_VALUE = "{VALUE}"
SUBSTITUTION_RANK = "{RANK}"
DEFAULT_NAME_SCHEME = SUBSTITUTION_VALUE + " OF " + SUBSTITUTION_RANK

ATTRIBUTE_SEARCH_KEY = r"^[A-Z]*.*[A-Z]$"

# Card Rank Ordered By Alphabetical Lowest To Highest
STANDARD_52_VALUES = {"ACE": "A", "TWO": "2", "THREE": "3", "FOUR": "4",
                      "FIVE": "5", "SIX": "6", "SEVEN": "7", "EIGHT": "8",
                      "NINE": "9", "TEN": "10", "JACK": "J", "QUEEN": "Q", "KING": "K"}
STANDARD_52_RANKS = {"SPADES": "\u2664", "CLUBS": "\u2667", 
                     "HEARTS": "\u2665", "DIAMONDS": "\u2666"}
STANDARD_52_VALUE_HIERARCHY = {"ACE": 13, "TWO": 1, "THREE": 2, "FOUR": 3,
                               "FIVE": 4, "SIX": 5, "SEVEN": 6, "EIGHT": 7,
                               "NINE": 8, "TEN": 9, "JACK": 10, "QUEEN": 11, "KING": 12}
STANDARD_52_RANK_HIERARCHY = {"SPADES": 4, "CLUBS": 1, 
                              "HEARTS": 3, "DIAMONDS": 2}
STANDARD_52_NAME_SCHEME = SUBSTITUTION_VALUE + SUBSTITUTION_RANK

class CardVariation:
  """
  Card Variation Should Have All Information Required To Create Card
  This class can be called upon to create custom card variations
  """
  def __init__(self, cardValues: Dict[str, str], cardRanks: Dict[str, str],
               valueHierarchy: Dict[str, str], rankHierarchy: Dict[str, str],
               priority: str = PRIORITY_NEUTRAL, nameScheme: str = DEFAULT_NAME_SCHEME) -> None:
    self.VALUES = type("Values", (object,), {})
    self.RANKS = type("Ranks", (object,), {})
    self.VALUE_HIERARCHY = type("ValueHierarchy", (object,), {})
    self.RANK_HIERARCHY = type("RankHierarchy", (object,), {})
    self.PRIORITY = priority
    self.NAME_SCHEME = nameScheme
    
    for valueKey in cardValues.keys(): setattr(self.VALUES, valueKey, cardValues[valueKey])
    for rankKey in cardRanks.keys(): setattr(self.RANKS, rankKey, cardRanks[rankKey])
    for valueHierKey in valueHierarchy.keys(): setattr(self.VALUE_HIERARCHY, valueHierKey, valueHierarchy[valueHierKey])
    for rankHierKey in rankHierarchy.keys(): setattr(self.RANK_HIERARCHY, rankHierKey, rankHierarchy[rankHierKey])

STANDARD_52 = CardVariation(STANDARD_52_VALUES, STANDARD_52_RANKS,
                            STANDARD_52_VALUE_HIERARCHY, STANDARD_52_RANK_HIERARCHY,
                            nameScheme=STANDARD_52_NAME_SCHEME)

class Card:
  """
  Ideally, this class is accessed using the Deck class. 
  However, for particular cases individual cards can be initialized

  Card should be able to:
  - self evaluate with other cards
  - print its value + rank
  - print its image
  - add cutomized printing scheme
  """
  def __init__(self, cardVariation: CardVariation,
                     value: str, rank: str, name: str = None) -> None:
    self._name = name
    self._value = value
    self._rank = rank
    self._image = None
    self._cardVariation = cardVariation

    if self._name is None:
      self._name = cardVariation.NAME_SCHEME.format(VALUE=value, RANK=rank)

  def __str__(self) -> str:
    return self._name

  def __eq__(self, __o: object) -> bool:
    assert(type(__o) is Card)
    return self._value == __o._value and self._rank == __o._rank

  def __ne__(self, __o: object) -> bool:
    assert(type(__o) is Card)
    return self._value != __o._value or self._rank != __o._rank

  def getValue(self) -> str:
    return self._value

  def getRank(self) -> str:
    return self._rank

  def getName(self) -> str:
    return self._name

  def getImage(self):
    return self._image
  
  def getCardVariation(self) -> CardVariation:
    return self._cardVariation

class Deck:
  def __init__(self, cardVariation: CardVariation, randomInit: bool = True) -> None:
    self._deck = [Card(cardVariation, getattr(cardVariation.VALUES, cardValue), getattr(cardVariation.RANKS, cardRank))
                  for cardValue in dir(cardVariation.VALUES) if re.search(ATTRIBUTE_SEARCH_KEY, cardValue) is not None
                  for cardRank in dir(cardVariation.RANKS) if re.search(ATTRIBUTE_SEARCH_KEY, cardRank) is not None]
    self._length = len(self._deck)
    self._cardVariation = cardVariation
    self._randomInit = randomInit
    if self._randomInit:
      random.shuffle(self._deck)

  def __str__(self) -> str:
    string = "Number of Cards In Deck: " + str(self._length) + "\nOrder:\n"
    for i in range(self._length):
      string += str(self._deck[i]) + "\n"
    return string
  
  def __len__(self) -> int:
    return self._length
  
  def getDeckSize(self) -> int:
    return self._length

  def setRandomInit(self, randomInit: bool) -> None:
    self._randomInit = randomInit

  def search(self, searchCard: Card) -> int:
    """
    Finds specified card in the deck
    If found, return index in deck, -1 otherwise
    """
    for i in range(self._length):
      if searchCard == self._deck[i]:
        return i
    return -1

  def draw(self, numCards: int = 1) -> Tuple[bool, List[Card]]:
    """
    Draws the number of cards specified
    returns true if drawn, false otherwise
    """
    drawnCards = []
    if self._length >= numCards:
      self._length -= numCards
      for i in range(numCards):
        drawnCards.append(self._deck.pop())
    return len(drawnCards) > 0, drawnCards

  def shuffle(self) -> None:
    """
    Shuffles current remaining cards
    """
    if self._length > 0:
      random.shuffle(self._deck)

  def reset(self):
    """
    Reinitializes the deck to default
    """
    self.__init__(self._cardVariation, self._randomInit)


if __name__ == "__main__":
  # card = Card(STANDARD_52, STANDARD_52.VALUES.ACE, STANDARD_52.RANKS.SPADES)
  # card2 = Card(STANDARD_52, STANDARD_52.VALUES.ACE, STANDARD_52.RANKS.SPADES)
  deck = Deck(STANDARD_52)
  ret, cards = deck.draw()
  print(deck)
  deck.setRandomInit(False)
  deck.reset()
  print(deck)