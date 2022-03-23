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


class CardType:
  CUSTOM = -1
  STANDARD_52 = 0
  TAROT = 1
  HANAFUDA = 2

class CardValue:
  pass

class CardRank:
  pass

class ValueHierarchy:
  pass


class RankHierarchy:
  pass


class BasicCard:
  """
  Ideally, this class is accessed using the Deck class. 
  However, for particular cases individual cards can be initialized
  """
  def __init__(self, name: str = "", value: CardValue = "", ) -> None:
    self._name = ""
    self._value = 0
    self._rank = 0
    self._image = 0



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