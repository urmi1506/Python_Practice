import random

# Get digits from a number as a list
def get_digits(num):
    return [int(d) for d in str(num)]

# Check if all digits are unique
def has_unique_digits(num):
    digits = get_digits(num)
    return len(digits) == len(set(digits))

# Generate a 4-digit number with unique digits
def generate_secret_number():
    while True:
        num = random.randint(1000, 9999)
        if has_unique_digits(num):
            return num

# Count bulls (correct digit & position) and cows (correct digit, wrong position)
def count_bulls_and_cows(secret, guess):
    bulls = cows = 0
    secret_digits = get_digits(secret)
    guess_digits = get_digits(guess)

    for i in range(4):
        if guess_digits[i] == secret_digits[i]:
            bulls += 1
        elif guess_digits[i] in secret_digits:
            cows += 1

    return bulls, cows

# Game starts here
secret_number = generate_secret_number()
tries = int(input("How many tries do you want? "))

while tries > 0:
    guess = int(input("Enter your 4-digit guess: "))

    # Check for valid input
    if guess < 1000 or guess > 9999:
        print("Please enter a 4-digit number.")
        continue
    if not has_unique_digits(guess):
        print("Digits must be unique. Try again.")
        continue

    bulls, cows = count_bulls_and_cows(secret_number, guess)
    print(f"{bulls} Bulls, {cows} Cows")

    if bulls == 4:
        print("You guessed it right")
        break

    tries -= 1

else:
    print(f"Out of tries .The number was: {secret_number}")
