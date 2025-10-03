import random

def user_guess():
    try:
        start = int(input("Enter the starting range: "))
        end = int(input("Enter the ending range: "))
    except ValueError:
        print("❌ Invalid range input. Please enter numbers only.")
        return

    num_generated = random.randint(start, end)
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Guess the number between {start} and {end}: "))
            if guess < num_generated:
                print("Too low! 👇")
            elif guess > num_generated:
                print("Too high! ☝️")
            else:
                print(f"🎉 Congratulations! You guessed the number {num_generated}!")
                return
            attempts += 1
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

    print(f"😢 Out of attempts! The number was {num_generated}.")

def computer_guess():
    print("🤖 Let me guess the number you're thinking of!")
    try:
        low = int(input("Enter the starting range: "))
        high = int(input("Enter the ending range: "))
    except ValueError:
        print("❌ Invalid range input. Please enter numbers only.")
        return

    print(f"Think of a number between {low} and {high}.")
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"🎉 I guessed your number in {attempts} attempts!")
            return
        else:
            print("❌ Invalid input. Please enter H, L, or C.")

def make_selection():
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME!")
    mode = input("Type (1) if YOU want to guess, or (2) if the COMPUTER should guess: ")

    if mode == '1':
        user_guess()
    elif mode == '2':
        computer_guess()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

make_selection()
