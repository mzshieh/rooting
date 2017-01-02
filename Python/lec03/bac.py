# 使用亂數套件
import random

def getA(guess, ans):
    ret = 0
    for i in range(4):
        if guess[i] == ans[i]:
            ret += 1
    return ret

def getB(guess, ans):
    ret = 0
    for i in range(4):
        # if guess[i] in ans[:i] or guess[i] in ans[i+1:]:
        if guess[i] != ans[i] and guess[i] in ans:
            ret += 1
    return ret

# 產生 0~9 的一個隨機整數，並且換成字串
ans = str(random.randint(0,9))
while len(ans) != 4:
    # 產生 0~9 的一個隨機整數，並且換成字串，作為下一位的候選人
    next_digit = str(random.randint(0,9))
    # 如果沒出現過，就加到答案後面
    if next_digit not in ans:
        ans = ans + next_digit

while True:
    # 使用者輸入
    guess = input('Guess a number: ')
    # 要四位 且 都是數字，一個沒有滿足就要重來
    if len(guess) != 4 or not guess.isdecimal():
        continue
    # 要不重複。重複的話，就把 flag 設定為 True
    flag = False
    for i in range(4):
        for j in range(4):
            if i !=j and guess[i]==guess[j]:
                flag = True
    # 有重複就重來
    if flag:
        continue

    # 猜對了就收工    
    if guess == ans:
        print('4A0B! You are correct!')
        break
    else:
        print('The answer is not',guess)
    # 猜錯給提示
    print(getA(guess,ans),'A',getB(guess,ans),'B',sep='')
