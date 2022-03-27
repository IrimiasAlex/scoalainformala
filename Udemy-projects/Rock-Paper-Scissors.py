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
# Printing my choice
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for papper or 2 for Scissors.\n"))

print(game_images[user_choice])

# Printing computer choice
computer_choice = random.randint(0,2)
print("computer_chose:")
print(game_images[computer_choice])

if user_choice < 0 and user_choice >= 3 :
  print("Invalid number. You lose!")
elif user_choice == 0 and computer_choice == 1:
  print("You lose!")
elif user_choice == 1 and computer_choice == 2:
  print("You lose!")
elif user_choice == 2 and computer_choice == 0:
  print("You lose!")
elif user_choice == computer_choice:
  print("It's a draw")
else:
  print("You win!")
