from brain_games.cli import welcome_user

name = None

def main():
    global user_name
    name = welcome_user()


if __name__ == '__main__':
    main()