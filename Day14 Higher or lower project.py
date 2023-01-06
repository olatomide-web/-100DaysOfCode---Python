from art import logo, vs
from game_data import data
import random


def format_data(account):
    account_name = account['name']
    account_follower_count = account['follower_count']
    account_description = account['description']
    account_country = account['country']

    return(f"{account_name}, a {account_description}, from {account_country}")


def check_answer(guess, A_follower_count, B_follower_count):
    if A_follower_count > B_follower_count:
        return guess == 'a'
    else:
            return guess == 'b'


print(logo)



score = 0
game_should_continue = True
account_B = random.choice(data)



while game_should_continue:

    account_A = account_B
    account_B = random.choice(data)


    if account_A == account_B:
        account_B = random.choice(data)

    print(f"compare A: {format_data(account_A)}")
    print(vs)
    print(f"against B: {format_data(account_B)}")



    guess = input("Who has more followers on instagram? Type 'A' or 'B': ").lower()



    account_A_follower_count = account_A['follower_count']
    account_B_follower_count = account_B['follower_count']


    is_correct = check_answer(guess, account_A_follower_count, account_B_follower_count)


    if is_correct:
        score = score + 1
        print(f"you are correct! current score is {score}")
    else:
        game_should_continue = False
        print(f"you are wrong! Final score is {score}")

                    
