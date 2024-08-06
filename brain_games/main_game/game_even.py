import prompt
from random import randint


def game_rules():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    
    
def user_answer():
    answer = prompt.string("Your anwser:")
    
    
def question():
    rand_numb = randint(0,100)
    print("Question:", rand_numb)
    return rand_numb



