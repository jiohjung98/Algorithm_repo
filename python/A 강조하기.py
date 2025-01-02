# def solution(myString):
#     arr = []
#     for elem in myString:
#         if elem == 'a':
#             arr.append('A')
#         elif elem !='A' and elem.upper():
#             arr.append(elem.lower())
#         else:
#             arr.append(elem)
#     return ''.join(arr)

def solution(myString):
    return myString.lower().replace('a', 'A')