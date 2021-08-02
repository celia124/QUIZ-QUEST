import requests
import random
from html import unescape
from random import choice

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

def get_questions(difficulty):
    ''''''
    if difficulty == "":
        #something something something
    #blah
        pass


    return questions


while True:
    response = requests.get('https://opentdb.com/api.php?amount=10&category=15&type=multiple')

    questions4 = response.json()['results']

    response_easy = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple')

    questions1 = response_easy.json()['results']

    response_med = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=medium&type=multiple')

    questions2 = response_med.json()['results']

    response_hard = requests.get('https://opentdb.com/api.php?amount=10&category=15&difficulty=hard&type=multiple')

    questions3 = response_hard.json()['results']

     # TODO clean this up


    print (''' 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME TO THE EPIC GAMER QUIZ MADE FOR GAMERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')
    gamemode = get_integer_input("What gamemode would you like \n Type 1 for easy \n Type 2 for medium \n Type 3 for hard \n Type 4 for a mix of all \n" , "That's not one of the options \n" , 0,5)
    if gamemode == 1:
        questions = questions1
    if gamemode == 2:
        questions = questions2
    if gamemode == 3:
        questions = questions3
    if gamemode == 4:
        questions = questions4
    num_correct = 0
    guesses = 0
    #this bit is a little confusing for me but its how the questions get in order and which one is correct.
    for i, question in enumerate(questions):
        print(f"Question {i + 1}")
        print(unescape(question['question']))
        all_answers = []
        all_answers.append(question['correct_answer'])
        for ans in question["incorrect_answers"]:
            all_answers.append(unescape(ans))
        random.shuffle(all_answers)
        for num, ans in enumerate(all_answers):
            print(f"{num+1}: {unescape(ans)}")
        correct_num = all_answers.index(question['correct_answer']) + 1
        print(correct_num)
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
    # if gamemode == 2:
    #     for i, question in enumerate(questions2):
    #         print(f"Question {i + 1}")
    #         print(unescape(question['question']))
    #         all_answers = []
    #         all_answers.append(question['correct_answer'])
    #         for ans in question["incorrect_answers"]:
    #             all_answers.append(unescape(ans))
    #         random.shuffle(all_answers)
    #         for num, ans in enumerate(all_answers):
    #             print(f"{num+1}: {unescape(ans)}")
    #         correct_num = all_answers.index(question['correct_answer']) + 1
    #         user_answer = get_integer_input("Write a number between 1 and 4 to get the answer ", "that is not one of the options", 0, 5)
    #         #this is the area that says if you got it wrong or right it's pretty simple but does the job
    #         if user_answer == correct_num:
    #             print("you got the right answer")
    #             print(f"the right answer is {correct_num}\n")
    #             guesses += 1
    #             num_correct += 1
    #         elif user_answer != correct_num:
    #             print("you got it wrong try the next question\n")
    #             print(f"the right answer is {correct_num}\n")
    #             guesses += 1
    # if gamemode == 3:
    #     for i, question in enumerate(questions3):
    #         print(f"Question {i + 1}")
    #         print(unescape(question['question']))
    #         all_answers = []
    #         all_answers.append(question['correct_answer'])
    #         for ans in question["incorrect_answers"]:
    #             all_answers.append(unescape(ans))
    #         random.shuffle(all_answers)
    #         for num, ans in enumerate(all_answers):
    #             print(f"{num+1}: {unescape(ans)}")
    #         correct_num = all_answers.index(question['correct_answer']) + 1
    #         user_answer = get_integer_input("Write a number between 1 and 4 to get the answer ", "that is not one of the options", 0, 5)
    #         #this is the area that says if you got it wrong or right it's pretty simple but does the job
    #         if user_answer == correct_num:
    #             print("you got the right answer")
    #             print(f"the right answer is {correct_num}\n")
    #             guesses += 1
    #             num_correct += 1
    #         elif user_answer != correct_num:
    #             print("you got it wrong try the next question\n")
    #             print(f"the right answer is {correct_num}\n")
    #             guesses += 1
    # if gamemode == 4:
    #     for i, question in enumerate(questions):
    #         print(f"Question {i + 1}")
    #         print(unescape(question['question']))
    #         all_answers = []
    #         all_answers.append(question['correct_answer'])
    #         for ans in question["incorrect_answers"]:
    #             all_answers.append(unescape(ans))
    #         random.shuffle(all_answers)
    #         for num, ans in enumerate(all_answers):
    #             print(f"{num+1}: {unescape(ans)}")
    #         correct_num = all_answers.index(question['correct_answer']) + 1
    #         user_answer = get_integer_input("Write a number between 1 and 4 to get the answer ", "that is not one of the options", 0, 5)
    #         #this is the area that says if you got it wrong or right it's pretty simple but does the job
    #         if user_answer == correct_num:
    #             print("you got the right answer")
    #             print(f"the right answer is {correct_num}\n")
    #             guesses += 1
    #             num_correct += 1
    #         elif user_answer != correct_num:
    #             print("you got it wrong try the next question\n")
    #             print(f"the right answer is {correct_num}\n")
    #             guesses += 1
    # i am trying to make a finishing question thing that tells you your score once you're done
    if guesses == 10:
        percent = num_correct * guesses
        print(f"~~~~~~~~~~~~~~~~You finished the quiz good job~~~~~~~~~~~~~~~~~~~~~ \nYou anwsered {percent}% of questions right")
    elif percent == 100:
        print("You got a perfect score")
    elif percent < 50 > 100:
        print ("You got a pass good job")
    else:
        print("You failed")
    break