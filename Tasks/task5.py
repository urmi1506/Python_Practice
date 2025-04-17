# Rock Paper Scissor Game
import random as rd


rock_table={"rock":"again","paper":"lose","scissor":"win"}
paper_table ={"paper":"again","scissor":"lose","rock":"win"}
scissor_table = {"scissor":"again","paper":"win","rock":"lose"}

game_table={"rock":rock_table,"paper":paper_table,"scissor":scissor_table}

ch = ["rock","paper","scissor"]

player_score = 0
computer_score = 0
round_no = 1

while True: 
  player = input("What do you want to play?: ").lower()
  print(f"Round {round_no}:")
  print(f"You played {player}!")
  computer = ch[rd.randint(0,2)]
  print(f"Computer played {computer}!")
  if game_table[player][computer] == "lose":
   print("Oh no! You Lose!")
   computer_score += 1
  if input(f"Your current score: {player_score}. Computer current score: {computer_score}. Another round? (Yes/No) ") == "No":
   break
  elif game_table[player][computer] == "win":
   print("Congrats! You Win!")
   player_score += 1
  if input(f"Your current score: {player_score}. Computer current score: {computer_score}. Another round? (Yes/No) ") == "No":
   break
  elif game_table[player][computer] == "again":
   print("Another round!")
  round_no += 1