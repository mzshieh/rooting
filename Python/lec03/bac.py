# 使用亂數套件
import random

# 產生 0~9 的一個隨機整數，並且換成字串
ans = str(random.randint(0,9))
while len(ans) != 4:
    # 產生 0~9 的一個隨機整數，並且換成字串，作為下一位的候選人
    next_digit = str(random.randint(0,9))
    # 如果沒出現過，就加到答案後面
    if next_digit not in ans:
        ans = ans + next_digit

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
