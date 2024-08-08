import prompt
from random import randint, choice


def game_rules():
    print('What is the result of the expression?')


def get_answer():
    return prompt.string('Your answer: ')


def question():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operation = choice(["-", "+", "*"])
    print("Question:", f'{number1} {operation} {number2}')
    return number1, operation, number2 


def correct_answer(question):
    number1, operation, number2 = question 
    return str(correct(number1, operation, number2))

def correct(number1, operation, number2):
    if operation == "-":
        return number1 - number2
    if operation == "+":
        return number1 + number2
    if operation == "*":
        return number1 * number2