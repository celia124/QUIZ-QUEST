import requests
import random
from html import unescape
from random import choice

def get_integer_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)



response = requests.get('https://opentdb.com/api.php?amount=10&category=15')

questions = response.json()['results']

print (''' 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO THE EPIC GAMER QUIZ MADE FOR GAMERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

num_correct = 0
guesses = 0
quiz_fin = False
while True:
    for i, question in enumerate(questions):
        print(f"question {i + 1}")
        print(unescape(question['question']))
        all_answers = []
        all_answers.append(question['correct_answer'])
        for ans in question["incorrect_answers"]:
            all_answers.append(unescape(ans))
        random.shuffle(all_answers)
        for num, ans in enumerate(all_answers):
            print(f"{num+1}: {unescape(ans)}")
        correct_num = all_answers.index(question['correct_answer']) + 1
        user_answer = get_integer_input("Write a number between 1 and 4 to get the answer\n", "that is not one of the options", 0, 5)
        if user_answer == correct_num:
            print("you got the right answer\n")
            guesses += 1
            num_correct += 1
        elif user_answer != correct_num:
            print("you got it wrong try the next question\n")
            guesses += 1
        print(guesses)
    quiz_fin = True
    if guesses == 10:

        if num_correct == 10:
            print("you got a perfect score good job you try again if wanted")
        if num_correct < 6 > 10:
            print("you almost got it you need to get a bit better knowledge in gaming")
        if num_correct < 1 > 6:
            print("you didn't get the best score")
        if num_correct == 0:
            print("you got none correct")