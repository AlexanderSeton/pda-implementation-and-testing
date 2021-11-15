### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:


  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   

  def highest_card(self, card1, card2):
    if self.check_for_ace(card1):
      return card1
    elif self.check_for_ace(card2):
      return card2
    elif card1.value > card2.value:
      return card1
    else:
      return card2
  


  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += 1
    return "You have a total of " + str(total)


# Task 1: Static Testing
  # line 11: = should be ==
  # line 13: else is missing :
  # line 17: dif not def
  # line 17: parameters missing , between car1 and card 2
  # line 18: if is not indented
  # line 19: should return card1
  # line 26: total should be assigned to 0
  # line 28: total should be incremented by 1 for every card, not by the cards value
  # line 29: return needs to be outdented
  # line 29: must make the int total a string 
  # line 25 - line 29: whole function needs to be indented
