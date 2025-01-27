def solution(s):
    answer = []
    arr = []
    # 튜플을 } 로 잘라서 탐색 시작
    for i in s.split("},"):
        # {, } 를 없애고 , 기준으로 push
        arr.append(i.replace("{", "").replace("}","").split(","))
    # 길이 순으로 정렬
    arr.sort(key=len)
    
    for i in arr:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer