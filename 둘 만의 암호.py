def solution(s, skip, index):
    answer_list = []
    index_list = []
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for alphabet in skip:
        alphabets.remove(alphabet)
    for char in s:
        new_index = alphabets.index(char) + index
        if (new_index) > len(alphabets)-1:
            index_list.append(new_index % len(alphabets))
        else:
            index_list.append(new_index)
    for x in index_list:
        answer_list.append(alphabets[x])
    answer = "".join(answer_list)
    return answer