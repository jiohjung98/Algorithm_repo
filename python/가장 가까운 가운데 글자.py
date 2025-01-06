
# 첫 번째 풀이: 효율성 별로 안좋음
# 1. ''.join(stack) 연산: 매번 문자열을 생성하는데 O(n) 시간
# 2. .find() 메서드: 최악의 경우 문자열 전체를 탐색해야 하므로 O(n) 시간
# 3. 리스트 수정: stack[''.join(stack).find(elem)] = ' '와 같은 수정 작업도 리스트 내부의 특정 위치를 찾고 값을 대체하는 작업이 포함되므로, 비효율적

# 복잡도 분석: for 반복문은 문자열 s의 길이 m만큼 반복됨
# 최악의 경우 시간 복잡도는 O(m * n)인데, 여기서 n은 stack의 길이(최대 m)이므로 O(m^2)

# def solution(s):
#     answer = []
#     stack = []
#     for idx, elem in enumerate(s):
#         if elem in stack:
#             answer.append(idx - ''.join(stack).find(elem))
#             stack[''.join(stack).find(elem)] = ' '
#             stack.append(elem)
#         else:
#             answer.append(-1)
#             stack.append(elem)
#     return answer


# 두 번째 풀이: 효율성 좋음
# 딕셔너리는 키를 기반으로 값을 조회하거나 갱신하는 작업이 평균적으로 O(1)

# 복잡도 분석: for 반복문은 문자열 s의 길이 m만큼 반복됨 -> O(m)
def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
    return answer
