from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)  # 몸무게 개수 저장
    
    for weight in count:
        # 같은 몸무게 조합 (nC2 = n * (n-1) / 2)
        answer += count[weight] * (count[weight] - 1) // 2  
        
        # 거리 비율에 따른 짝꿍 찾기
        for ratio in (2/3, 1/2, 3/4):
            target = weight * ratio
            if target in count:
                answer += count[weight] * count[target]
    
    return answer
