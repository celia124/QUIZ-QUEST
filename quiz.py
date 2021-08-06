import requests
import random
from html import unescape
from random import choice
import time
import msvcrt 


def get_integer_input(message, error, low, high):
    ''' '''
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)


def readch(echo=True):
    ch = msvcrt.getch()
    while ch in b'\x00\xe0': 
        msvcrt.getch()       
        ch = msvcrt.getch()
    if echo:
        msvcrt.putch(ch)
    return ch.decode()


def get_questions(difficulty):
    ''''''
    if difficulty == "":
        #something something something
    #blah
        pass

    return questions


#this is to get the difficulty and stuff
response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=multiple')

questions4 = response.json()['results']

response_easy = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple')

questions1 = response_easy.json()['results']

response_med = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=medium&type=multiple')

questions2 = response_med.json()['results']

response_hard = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=hard&type=multiple')

questions3 = response_hard.json()['results']


print (''' 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO THE EPIC GAMER QUIZ MADE FOR GAMERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
# This is to get which gamemode they want
gamemode = get_integer_input("What gamemode would you like \n Type 1 for easy \n Type 2 for medium \n Type 3 for hard \n Type 4 for a mix of all \n" , "That's not one of the options \n" , 0,5)
if gamemode == 1:
    questions = questions1
if gamemode == 2:
    questions = questions2
if gamemode == 3:
    questions = questions3
if gamemode == 4:
    questions = questions4
gamemode1 = get_integer_input("Do you want a Normal game, Timed \n Type 1 for Normal \n Type 2 for Timed \n Type 3 for a limited amount of time \n ", "That is not an option", 0,4)
if gamemode1 == 2:
    start = time.time()
if gamemode1 == 3:
    max_time = get_integer_input("You can have a time between 1-120 seconds\n", "That is not a time that can be choosen\n", 0,121)
    def readch(echo=True):
        ch = msvcrt.getch()
        while ch in b'\x00\xe0':
            msvcrt.getch()
            ch = msvcrt.getch()
        if echo:
            msvcrt.putch(ch)
            return ch.decode()
    def elapsed_time():
        global start_time
        return time.time() - start_time
    start_time = time.time()
    while elapsed_time() < max_time:



        num_correct = 0
        guesses = 0


        #this bit is a little confusing for me but its how the questions get in order and which one is correct.
        for i, question in enumerate(questions):
            print(f"Question {i + 1}")
            print(unescape(question['question']))
            question_answers = []
            question_answers.append(question['correct_answer'])
            for ans in question["incorrect_answers"]:
                question_answers.append(unescape(ans))
            random.shuffle(question_answers)
            for num, ans in enumerate(question_answers):
                print(f"{num+1}: {unescape(ans)}")
            correct_num = question_answers.index(question['correct_answer']) + 1
            user_answer = get_integer_input("Write a number between 1 and 4 to get the answer ", "that is not one of the options", 0, 5)
            #this is the area that says if you got it wrong or right it's pretty simple but does the job
            while elapsed_time() < max_time:
                if not msvcrt.kbhit():
                    time.sleep(0.1)
                else:
                    if user_answer == correct_num:
                        print("you got the right answer\n")
                        print(f"the right answer is {correct_num}\n")
                        guesses += 1
                        num_correct += 1
                    elif user_answer != correct_num:
                        print("you got it wrong try the next question\n")
                        print(f"the right answer is {correct_num}\n")
                        guesses += 1
                        break
            else:
                print()
        print()
        print("Times up")
                    


        if gamemode1 == 2:
            end = time.time()
        if guesses == 10:
            percent = num_correct * guesses
            print(f"~~~~~~~~~~~~~~~~You finished the quiz good job~~~~~~~~~~~~~~~~~~~~~ \nYou anwsered {percent}% of questions right")
            if gamemode1 == 2:
                print(f"You finished in {round(end-start,1)} seconds")
            if percent == 100:
                print("You got a perfect score")
            elif percent < 50 > 100:
                print ("You got a pass good job")
            else:
                print("You failed")
num_correct = 0
guesses = 0


#this bit is a little confusing for me but its how the questions get in order and which one is correct.
for i, question in enumerate(questions):
    print(f"Question {i + 1}")
    print(unescape(question['question']))
    question_answers = []
    question_answers.append(question['correct_answer'])
    for ans in question["incorrect_answers"]:
        question_answers.append(unescape(ans))
    random.shuffle(question_answers)
    for num, ans in enumerate(question_answers):
        print(f"{num+1}: {unescape(ans)}")
    correct_num = question_answers.index(question['correct_answer']) + 1
    user_answer = get_integer_input("Write a number between 1 and 4 to get the answer ", "that is not one of the options", 0, 5)
    #this is the area that says if you got it wrong or right it's pretty simple but does the job
    if user_answer == correct_num:
        print("you got the right answer\n")
        print(f"the right answer is {correct_num}\n")
        guesses += 1
        num_correct += 1
    elif user_answer != correct_num:
        print("you got it wrong try the next question\n")
        print(f"the right answer is {correct_num}\n")
        guesses += 1


if gamemode1 == 2:
    end = time.time()
if guesses == 10:
    percent = num_correct * guesses
    print(f"~~~~~~~~~~~~~~~~You finished the quiz good job~~~~~~~~~~~~~~~~~~~~~ \nYou anwsered {percent}% of questions right")
    if gamemode1 == 2:
        print(f"You finished in {round(end-start,1)} seconds")
    if percent == 100:
        print("You got a perfect score")
    elif percent < 50 > 100:
        print ("You got a pass good job")
    else:
        print("You failed")