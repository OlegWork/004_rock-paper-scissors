import random

rock_pick = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        '''
paper_pick = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
            '''
scissors_pick = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
            '''

figures = [rock_pick, paper_pick, scissors_pick]
options = ["Rock", "Paper", "Scissors"]
user_choise = int(input("Chose rock (0), paper (1), scisors (2)\n"))
computer_choise = random.randint(0, 2)
print(figures[user_choise])
user_choise = options[user_choise]
print(f"You choose {user_choise}")
print(figures[computer_choise])
computer_choise = options[computer_choise]
print(f"Computer choose {computer_choise}")



if user_choise == computer_choise:
    print("It's a draw!")
elif user_choise == "Rock" and computer_choise == "Scissors":
    print("You won")
elif user_choise == "Scissors" and computer_choise == "Rock":
    print("Computer won")
elif user_choise == "Rock" and computer_choise == "Paper":
    print("Computer won")
elif user_choise == "Paper" and computer_choise == "Rock":
    print("You won")
elif user_choise == "Paper" and computer_choise == "Scissors":
    print("Computer won")
elif user_choise == "Scissors" and computer_choise == "Paper":
    print("Computer won")
else:
    print("Wrong data")
