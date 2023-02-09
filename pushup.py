#! /usr/bin/python3
# usage: ./pushup.py

import sys
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('cards', metavar='N', type=int, help='number of cards to pull')

args = parser.parse_args()

# function to print your card results
def print_card( number ):
  
  # actual card face value
  face_value = int(number % 13)
  if face_value == 0:
      face = 'joker'
  elif 0 < face_value < 10:
     face = face_value
  elif face_value == 10:
     face = "jack"
     face_value = 10
  elif face_value == 11:
     face = "queen"
     face_value = 10
  elif face_value == 12:
     face = "king"
     face_value = 10
  elif face_value == 13:
     face = "ace"
     face_value = 10

  # card suit based off modulo value
  dumb = int(number / 13)
  suit = " "
  if dumb == 0:
    suit = "hearts"
  elif dumb == 1:
    suit = "diamonds"
  elif dumb == 2:
    suit = "spades"
  elif dumb == 3:
    suit = "clubs"
  elif face == "joker":
    suit = "joker"
  else:
    suit = "hearts"

  # temporary print job to show original values
  print( f' {str(face)} of {suit}')
  return face_value

# initialization of some variables
cards = []
i = 1
total = 0

# prepopulate the deck of cards into list
while i < 53:
 cards.append(i)
 i += 1

# randomly select cards from list, using function to translate from 1-52 to names
i = 0
while i < args.cards:
  card = random.choice(cards)
  total += int(print_card(card))
  i += 1

print(f'Your total is {str(total)}')
