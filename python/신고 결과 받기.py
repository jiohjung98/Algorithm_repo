def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x:0 for x in id_list}

    for y in set(report):
        reports[y.split()[1]] += 1
        
    for z in set(report):
        if reports[z.split()[1]] >= k:
            answer[id_list.index(z.split()[0])] += 1
    return answer