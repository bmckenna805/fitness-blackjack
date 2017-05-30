#! /usr/bin/python
# usage: ./pushup.py 

import sys
import random

def print_card(number):
  a = int(number / 13)
  b = int(number % 13)
  print a
  print b

print "Enter the number of cards to pull"
sample_size = int(raw_input())

cards = []
i = 1

while i < 53:
 cards.append(i)
 i += 1

y = 0
while y < sample_size:
  card = random.choice(cards)
  print_card(card)
  y += 1
