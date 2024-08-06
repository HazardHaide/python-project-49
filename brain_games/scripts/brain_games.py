from brain_games.cli import welcome_user

name = None


def main():
    global name
    name = welcome_user()


if __name__ == '__main__':

    main()
