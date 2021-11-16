### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.


class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```

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




Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python