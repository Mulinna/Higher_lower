import random
from game_data import data
comparison_A = 0
comparison_B = 0
comparison_C = 0
global_winner = 0


def dictionaries():
  first_dictionary = random.choice(data)
  global comparison_A
  comparison_A = first_dictionary
  second_dictionary = random.choice(data)
  global comparison_B
  comparison_B = second_dictionary
  third_dictionary = random.choice(data)
  global comparison_C
  comparison_C = third_dictionary
  if first_dictionary == second_dictionary or second_dictionary == third_dictionary:
    dictionaries()

dictionaries()

def correct_answer(comparison_A, comparison_B, answer, winner):
  score_A = int((comparison_A['follower_count']))
  score_B = int((comparison_B['follower_count']))
  if score_A > score_B:
    winner == "A"
  elif score_B > score_B:
    winner == "B"
  global global_winner
  global_winner = winner

  
def game(comparison_A, comparison_B):
  print(f"Compare A: {(comparison_A['name'])}, {(comparison_A['description'])}, from {(comparison_A['country'])}.")
  print(f"Compare B: {(comparison_B['name'])}, {(comparison_B['description'])}, from {(comparison_B['country'])}.")
  answer = input("Who has more followers? A or B? ")
  if answer == winner:
    
  


  

correct_answer(comparison_A, comparison_B, answer, winner)
game(comparison_A, comparison_B)
