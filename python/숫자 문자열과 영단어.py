# def solution(s):
#     arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
#     tmp = ''
#     tmp2 = ''
#     for elem in s:
#         if elem.isdigit():
#             tmp += elem
#         else:
#             tmp2 += elem
#             if tmp2 in arr:
#                 tmp += str(arr.index(tmp2))
#                 tmp2 = ''

#     return int(tmp)
        
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

