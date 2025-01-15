def solution(wallet, bill):
    cnt = 0
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        bigger_idx = bill.index(max(bill))
        bill[bigger_idx] //= 2
        cnt += 1
    return cnt