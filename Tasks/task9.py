# Guess The Number Game

import random as rd

while True:
    num = rd.randint(1, 9)
    print("Guess the no when program ask you...")
    
    # which no guess first
    guess = None
    # how many time guess no
    guess_no = 1

    while True:
        guess = int(input("Guess The Number:"))
        print(guess)

        if guess > num: 
            print("Guess No is High") 
            guess_no += 1
        elif guess < num:
            print("Guess No is Low") 
            guess_no += 1
        elif guess == num: 
            print(f"Guess Exact No....Congrats!!! You take {guess_no} no of attempts") 
            break

    if input("Do you want to play again? (Yes/NO): ") == "NO":
        break
