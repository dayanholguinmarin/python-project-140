from brain_games.cli import welcome_user
from random import randint
import prompt
import math
name = welcome_user()
def is_prime(name):
    for i in range(1, 4): # Repite 3 
        random_number = randint(1, 100)

        for i in range(2, int(math.sqrt(random_number)) + 1):
            if random_number % i == 0:
                correct_answer = 'no'
                break            
        else:
            correct_answer = 'yes'

        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        question = prompt.string(f'Question: {random_number}')

        if question not in ['yes', 'no']:
            print('Invalid answer. Please answer "yes" or "no".')
            return

        if question == correct_answer:
            print('Correct!')
        else:
            print(f'{question} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
       

