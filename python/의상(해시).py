# Counter : 데이터의 개수를 셀 때 유용
# Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
# -> Counter({'blue': 3, 'red': 2, 'green': 1})

# reduce : 여러 개의 데이터를 대상으로 주로 누적 집계에 사용
# reduce(집계 함수, 순회 가능한 데이터[, 초기값])
# 집계 함수는 두개의 인자를 받음
# 첫번째 인자 : 누적자(accumulator) - 함수 실행의 시작부터 끝까지 계속 재사용 값
# 두번째 인자 : 현재값(current value) - 현재값은 루프 돌면서 계속해서 바뀌는 값
# -> reduce(lambda acc, cur: acc + cur["age"], users, 0)

from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x,y: x*(y+1), cnt.values(), 1) -1
    return answer