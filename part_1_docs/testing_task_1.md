### Testing task 1:

# Carry out static testing on the code below.

# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # = operator indicates we're assiging values but this should have == operator to indicate comparison for the if statement like so: if card.value == 1;
      return True
    else # missing colon after the else statement
      return False


  dif highest_card(self, card1 card2): # 1) spelling error as it needs to be 'def' to define the method and 2) it's missing a comma between "card1" and "card2" to indicate they're two different arguments
  if card1.value > card2.value: # lines 29-32 should be indented to indicate it's a part of the "highest_card" method
    return card # "card doesn't exist, should be "card1"
  else:
    return card2
    # no statement to indicate what to do if card1.value == card2.value



def cards_total(self, cards): # lines 37-41 not indented to indicate "cards_total" is part of CardGame class
  total # no declaration of what total should be, so should be total = 0;
  for card in cards:
    total += card.value
    return "You have a total of" + total # 1) return should be outside of the loop and 2) statement incorrectly concatenated so should be: f"You have a total of {total}"

```
