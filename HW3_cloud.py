import random
import copy


def random_four_number():
    """產出四個 0~9 數字的list，當中數字不能重複"""
    nums = [_ for _ in range(0, 10)]
    ret = []
    for _ in range(4): # 跑四次
        index = random.randint(0, len(nums) - 1)
        num = nums[index]
        ret.append(num)
        nums.remove(num)
    return ret


def user_input():
    """讓使用者輸入四個數字，輸入的數字不能重複，不能為數字以外的東西"""
    from_user = input('請輸入答案: ')
    try:
        if len(set(from_user)) != 4:
            print('請輸入4個不重複的數字')
            return None, None
        return from_user, [int(item) for item in from_user]
    except:
        print('請輸入4個數字')
        return None, None


def find_a(user_input_list: list, answer: list) -> tuple:
    a = 0
    new_list = copy.copy(user_input_list)
    for index, num in enumerate(user_input_list):
        if answer[index] == num:
            new_list.remove(num)
            a += 1
    return a, new_list


def find_b(new_list: list, answer: list) -> int:
    b = 0
    for num in set(new_list):
        if num in answer:
            b += 1
    return b


def game_logic(answer, user_input_list):
    ans_a, list_without_a_ans = find_a(user_input_list, answer)
    ans_b = find_b(list_without_a_ans, answer)
    return ans_a, ans_b


def main(answer: list, limit: 0) -> bool:
    count = 1
    while limit - count >= 0:
        from_user, user_input_list = user_input()
        if not user_input_list:
            continue
        if user_input_list == answer:
            print(f"猜對了，答案為：{answer}，總共猜了 {count} 次")
            return True
        count += 1
        ans_a, ans_b = game_logic(answer, user_input_list)
        print(f"{ans_a}A{ans_b}B")
    print(f"遊戲結束，超過限制次數 {limit}")
    return False


if __name__ == "__main__":
    answer = random_four_number()
    print(answer)  # debug
    main(answer, limit=8)
    # ans_a, ans_b = game_logic(answer, [1, 2, 3, 4])
    # answers = []
    # for _1 in range(0, 10):
    #     for _2 in range(0, 10):
    #         for _3 in range(0, 10):
    #             for _4 in range(0, 10):
    #                 answers.append([_1, _2, _3, _4])
    # f = filter(lambda x: x if len(set(x)) == 4 else None, answers)
    # unique_answers = [_ for _ in f]
    # print(unique_answers)
    # def b_game_logic(answer: list, guess: list):
    #     correct = incorrect = n = 0
    #     for i in guess:
    #         if int(guess[n]) == answer[n]:
    #             correct += 1
    #         elif int(i) in answer:
    #             incorrect += 1
    #         elif guess == answer:
    #             correct = 4
    #             break
    #         elif correct == 4:
    #             break
    #         n += 1
    #     return correct, incorrect
    #
    # for try_ans in answers:
    #     if len(set(try_ans)) < 4:
    #         continue
    #     try:
    #         assert b_game_logic(answer, try_ans) == game_logic(answer, try_ans)
    #     except AssertionError:
    #         print(answer, try_ans, b_game_logic(answer, try_ans), game_logic(answer, try_ans))
    #         continue
