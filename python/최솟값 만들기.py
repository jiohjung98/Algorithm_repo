def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    ans_arr = [x * y for x, y in zip(A,B)]
        
    return sum(ans_arr)