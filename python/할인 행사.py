from collections import Counter

def solution(want, number, discount):
    answer = 0
    discount_days = sum(number)
    want_dict = dict(zip(want,number))
    repeat_count = len(discount) - discount_days + 1
    for i in range(repeat_count):
        if want_dict == Counter(discount[i:i+discount_days]):
            answer += 1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

solution(want, number, discount)