def solution(people, limit):
    people.sort()
    answer = 0
    start_idx = 0
    end_idx = len(people) - 1
    
    while start_idx < end_idx:
        if people[start_idx] + people[end_idx] <= limit:
            start_idx += 1
            answer += 1
        end_idx -= 1
    return len(people) - answer