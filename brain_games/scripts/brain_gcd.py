from brain_games.cli import welcome_user
from random import sample, choice
import prompt

def random_mcd(): 
  number_1, number_2 = sample(range(1, 100), 2)
  return number_1, number_2

def gcd(a, b):
            while b:
                a, b = b, a % b    # algoritmo de Euclides para sacar el MCD
            return a


def mcd(name):
    for i in range(1, 4):  # Repite  3 veces
        number_1, number_2 = random_mcd()  # dos numeros aleatorios
        question = f'{number_1} {number_2}'
        
        correct_answer = gcd(number_1, number_2)
        
        print('Find the greatest common divisor of given numbers.')
        user_answer = prompt.string(f'Question: {question}')
        
        if int(user_answer) == correct_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            return
    
    print(f'Congratulations, {name}!')  

def main():
    name = welcome_user()
    mcd(name)
    
if __name__ == "__main__":
    main()