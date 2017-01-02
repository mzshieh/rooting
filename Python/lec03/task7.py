# 使用亂數套件
import random

# 產生 0~9 的一個隨機整數
ans = random.randint(0,9)

for i in range(5):
    guess = input('Guess a number: ')
    while not type(guess)==type(0):
        try:
            guess = int(guess)
        except:
            guess = input('Guess a number: ')
            continue
    
    if guess == ans:
        break
    else:
        print('The answer is not',guess)
    if guess < ans:
        print('The answer is greater.')
    else:
        print('The answer is less.')

if guess == ans:
    print('You are right. The answer is',ans)
else:
    print('The answer is',ans)
