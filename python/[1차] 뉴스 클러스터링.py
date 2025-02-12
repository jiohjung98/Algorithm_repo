# 입력 문자열 2글자씩 끊어야 함
# 영문자로 된 글자쌍만 유효
from collections import Counter

def solution(str1, str2):
    answer = 0
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_arr = []
    str2_arr = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_arr.append(str1_low[i] + str1_low[i+1])
    for i in range(len(str2_low)-1):
        if str2_low[i].isalpha() and str2_low[i+1].isalpha():
            str2_arr.append(str2_low[i] + str2_low[i+1])
    
    Counter1 = Counter(str1_arr)
    Counter2 = Counter(str2_arr)
    x = list((Counter1 & Counter2).elements())
    y = list((Counter1 | Counter2).elements())
    
    if len(x) == 0 and len(y) == 0:
        return 65536
    return int((len(x) / len(y)) * 65536)
