from brain_games.cli import welcome_user
from random import randint
import prompt


def random_number():
    return randint(1, 100)


def first_question(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(1, 4):
        number = random_number()
        is_even = number % 2 == 0
        VALID_ANSWER = ['yes', 'no']
        correct_answer = 'yes' if is_even else 'no'
        question = prompt.string(f'Question: {number}')


        if question not in VALID_ANSWER:
            break

        if question == correct_answer:
            print(f'Correct!')

        else:
            print((
                f"'{question}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            ))
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    first_question(name)


if __name__ == "__main__":

    main()

