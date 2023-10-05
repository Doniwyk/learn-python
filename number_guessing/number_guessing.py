import random

EASY = 10
HARD = 5


def check_answer(answer, turns, guess):
    if guess > answer:
        print("Too high, guess again")
        return turns - 1
    elif guess < answer:
        print("Too low, guess again")
        return turns - 1
    else:
        print("=== YOU WIN ===")


def choose_difficulty():
    difficulty = input("Choose difficulty, type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY
    else:
        return HARD


def game():
    print("============================")
    print("=== NUMBER GUESSING GAME ===")
    print("===       1 - 100        ===")
    print("============================")
    answer = random.randint(1, 100)
    turns = choose_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempt left")
        guess = int(input("Your guess: "))
        turns = check_answer(answer, turns, guess)

        if turns == 0:
            print("=== YOU LOSE! ===")
            return


game()
