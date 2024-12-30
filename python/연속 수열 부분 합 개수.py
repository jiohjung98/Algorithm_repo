def solution(elements):
    lengths = len(elements)
    ans = set()
    
    for i in range(lengths):
        tmp = elements[i]
        ans.add(tmp)
        for j in range(i+1, i+lengths):
            tmp += elements[j%lengths]
            ans.add(tmp)
    return len(ans)