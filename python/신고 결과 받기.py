# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x:0 for x in id_list}

#     for y in set(report):
#         reports[y.split()[1]] += 1
        
#     for z in set(report):
#         if reports[z.split()[1]] >= k:
#             answer[id_list.index(z.split()[0])] += 1
#     return answer

def solution(id_list, report, k):
    report_dict = {user: set() for user in id_list}
    report_count = {user: 0 for user in id_list}
    
    for elem in report:
        reporter, reported = elem.split(' ')
        if reported not in report_dict[reporter]:
            report_dict[reporter].add(reported)
            report_count[reported] += 1
    
    banned_user = {user for user, count in report_count.items() if count >= k}
    answer = [0] * len(id_list)
    for i, user in enumerate(id_list):
        answer[i] += len(report_dict[user] & banned_user)
    return answer