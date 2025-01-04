# def solution(s):
#     if (len(s) == 4 or len(s) == 6) and s.isdigit():
#         return True
#     else:
#         return False
    
def solution(s):
    return True if len(s) in (4,6) and s.isdigit() else False