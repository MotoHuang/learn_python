import random
def create_random_number():
    print("請輸入要生成幾個數字的答案")
    answer_num = int(input())
    answer = random.sample(range(0, 9), answer_num)

print("請輸入正確答案")
start = True
correct = incorrect = 0

while start:
    guess=list(input())
    count = 0
    while count < len(answer_num):
        if answer[count] == guess[count]:
            correct += 1
            count += 1
            break
        else:
            incorrect += 1
            break
    print(correct, "A" , incorrect, "B")
