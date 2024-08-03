import random
from game_data import data
comparison_A = 0
comparison_B = 0

def dictionaries():
  first_index = random.randint(0, len(data) -1)
  first_dictionary = data[first_index]
  global comparison_A
  comparison_A = first_dictionary
  second_index = random.randint(0, len(data) -1)
  second_dictionary = data[second_index]
  global comparison_B
  comparison_B = second_dictionary
  if first_dictionary == second_dictionary:
    dictionaries()

dictionaries()

def game(comparison_A, comparison_B):
  print(f"Compare A: {(comparison_A['name'])}, {(comparison_A['description'])}, from {(comparison_A['country'])}.")
  print(f"Compare B: {(comparison_B['name'])}, {(comparison_B['description'])}, from {(comparison_B['country'])}.")

game(comparison_A, comparison_B)
