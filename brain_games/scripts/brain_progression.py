from brain_games.cli import welcome_user
from random import randint
import prompt


def progression(name):
    for i in range(1, 4):
        progresion_items = randint(5, 10)
        progresion_Number = randint(1, 10)
        progresion_step = randint(1, 5)
        empty_list = []
        for j in range(progresion_items):
          current_number = progresion_Number + j * progresion_step
          empty_list.append(current_number)

        missing_index = randint(0, len(empty_list) - 1)
        correct_answer = empty_list[missing_index]
        empty_list[missing_index] = '..'

        question = ' '.join([str(x) for x in empty_list])

        print('What number is missing in the progression?')
        user_answer = prompt.string(f'Question: {question}')

        if int(user_answer) == correct_answer:
            print('Correct!')
        else:
            print((
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            ))
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    progression(name)


if __name__ == "__main__":

    main()