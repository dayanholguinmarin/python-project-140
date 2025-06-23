from brain_games.cli import welcome_user
from random import sample, choice
import prompt

def random_math_number(): 
  number_1, number_2 = sample(range(1, 100), 2)
  return number_1, number_2

name = welcome_user()
def calculate(name):
    for i in range(1, 4):  # Repite  3 veces
        number_1, number_2 = random_math_number()  # dos numeros aleatorios
        operators = ['+', '-', '*']
        random_operation = choice(operators)  # operadores aleatorio
        question = f'{number_1} {random_operation} {number_2}'
        
        match random_operation:
            case '+':
                correct_answer = number_1 + number_2
            case '-':
                correct_answer = number_1 - number_2
            case '*':
                correct_answer = number_1 * number_2
            case _:
                correct_answer = number_1 + number_2

        
        print('What is the result of the expression?')
        user_answer = prompt.string(f'Question: {question}')
        
        if  int(user_answer) == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            return  
    
    print(f'Congratulations, {name}!')  