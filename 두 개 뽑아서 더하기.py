# 두 개 뽑아서 더하기
# 문제 설명
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

def solution(numbers):
    answer = []
    numbers.sort()
    print(numbers)
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j] not in answer):
                answer.append(numbers[i] + numbers[j])    
    answer.sort()
    return answer

# set()을 이용한 풀이

# 리스트에 숫자를 추가하기 전에 이미 리스트에 존재하는지 확인하는 과정이 필요. 
# 이를 위해 answer 리스트를 집합(set)으로 선언하고, 숫자를 추가할 때도 집합의 add() 메서드를 사용하여 중복을 피할 수 있음. 
# 마지막에 리스트로 변환하여 반환하면 됨.

def solution(numbers):
    answer = set()
    numbers.sort()
    
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    
    return sorted(list(answer))
