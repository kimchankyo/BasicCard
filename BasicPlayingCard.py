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

from typing import Dict

PRIORITY_VALUE = "PRI_VALU"
PRIORITY_RANK = "PRI_RANK"
PRIORITY_NEUTRAL = "PRI_NEUT"
DEFAULT_NAME_SCHEME = "\{VALUE\} OF \{RANK\}"

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
STANDARD_52_NAME_SCHEME = "\{VALUE\}\{RANK\}"

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
                            STANDARD_52_VALUE_HIERARCHY, STANDARD_52_RANK_HIERARCHY)

class Card:
  """
  Ideally, this class is accessed using the Deck class. 
  However, for particular cases individual cards can be initialized

  Card should be able to:
  - self evaluate with other cards
  - print its value + rank
  - print its image
  - add cutomized printing scheme

  Set functions
  - name
  - value
  - rank
  - image
  - value hierarchy
  - rank hierarchy
  """
  def __init__(self, value: str, rank: str, name: str = None) -> None:
    self._name = name
    self._value = value
    self._rank = rank

  def __repr__(self) -> str:
    if self._name is None:
      return self._value + " OF " + self._rank
    else:
      return self._name

class Deck:

  def __init__(self) -> None:
    pass

  def search(self):
    """
    Finds specified card in the deck
    """
    pass

  def draw(self, numCards: int = 1):
    """
    Draws the number of cards specified
    """
    pass

  def shuffle(self):
    """
    Shuffles current remaining cards
    """
    pass

  def reset(self):
    """
    Reinitializes the deck to default
    """
    pass


  if __name__ == "__main__":
    name = STANDARD_52.VALUES.ACE + STANDARD_52.RANKS.SPADES
    card = Card(STANDARD_52.VALUES.ACE, STANDARD_52.RANKS.SPADES)
    print(card)