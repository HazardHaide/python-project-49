import prompt
from brain_games.cli import welcome_user


def run_game(module):
    name = welcome_user()
    module.game_rules()
    count = 3
    for i in range(count):
        question = module.ask_question()
        answer = get_answer()
        if not is_correct_answer(module, question, answer):
            correct = module.get_correct_answer(question)
            game_over(name, answer, correct)
            break
        print('Correct!')
    else:
        win(name)


def game_over(name, answer, correct):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}')")
    print(f"Let's try again, {name}!")


def is_correct_answer(module, question, answer):
    correct = module.get_correct_answer(question)
    return correct == answer


def get_answer():
    return prompt.string('Your answer: ')


def win(name):
    print(f'Congratulations, {name}!')