import random
import sys
answer = []
guess = []

def create_random_number():
    print('開始產生四位數隨機不重複數字')
    answer = random.sample(range(0, 9), 4)
    return answer

def game_logic(answer:list, guess:list):
    correct = incorrect = n = 0
    for i in guess:
        if int(guess[n]) == answer[n]:
            correct += 1
        elif int(i) in answer:
            incorrect += 1
        elif guess == answer:
            correct = 4
            break
        elif correct == 4:
            break
        n += 1
    return correct, incorrect

def number_repeat(guess:list):
    guess_new = []                  #判斷輸入的字串是否重複
    for j in guess:                 #新增一個空字串,把原本字串放進去
        if j not in guess_new:      #把不重複的放進新字串
            guess_new.append(j)
    if len(guess) != len(guess_new):#如果舊字串與新字串長度相同,代表沒有重複值
        print('數字重複')

answer = create_random_number()
while True:
    guess = list(input('請輸入正確答案:'))
    number_repeat(guess)
    correct, incorrect = game_logic(answer, guess)
    if correct == 4:
        sys.exit(f'答對了!答案是{answer}\nGood Bye!')
    else:
        print(f'{correct}A {incorrect}B')