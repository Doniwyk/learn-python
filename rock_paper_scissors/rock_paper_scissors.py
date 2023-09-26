import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img = [rock, paper, scissors]
outcomes = ["It's a tie!", "You win!", "Computer wins!"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

print(f"You chose:\n{img[user_choice]}")
print(f"Computer chose:\n{img[computer_choice]}")

result = (user_choice - computer_choice) % 3

print(outcomes[result])
