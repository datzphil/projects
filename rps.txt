# Write your code here
from random import choice

IS_RUNNING = True
DRAW_SCORE = 50
WIN_SCORE = 100
winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}


def draw():
    if name_input in rating_system:
        rating_system[name_input] += DRAW_SCORE


def win():
    if name_input in rating_system:
        rating_system[name_input] += WIN_SCORE


rating_system = {}
name_input = input("Enter your name: ")
print(f'Hello, {name_input}')
file = open('rating.txt', 'r+')
for line in file:
    user = line.split()
    rating_system[user[0]] = int(user[1])

file.close()
if name_input not in rating_system:
    rating_system[name_input] = 0
user_selection = input()
if user_selection == "":
    rps_list = ["rock", "paper", "scissors"]
else:
    rps_list = user_selection.split(',')
print("Okay, let's start")
while IS_RUNNING:
    computer_input = choice(rps_list)
    user_input = input()
    if user_input == "!rating":
        print(rating_system[name_input])
    elif user_input == "!exit":
        print("Bye!")
        exit()
    elif user_input not in rps_list:
        print("Invalid input")
    elif user_input == computer_input:
        print(f"There is a draw ({computer_input})")
        draw()
    elif computer_input not in winning_cases[user_input]:
        print(f"Sorry, but the computer chose {computer_input}")
    elif computer_input in winning_cases[user_input]:
        print(f"Well done. The computer chose {computer_input} and failed")
        win()
