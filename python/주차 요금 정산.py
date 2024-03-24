import math

def timeToMinutes(date):
    h, m = map(int, date.split(':'))
    return h * 60 + m

def solution(fees, records):
    answer = []
    dt, df, ut, uf = fees
    records_dic = dict()
    for r in records:
        time, num, history = r.split()
        num = int(num)
        if num in records_dic:
            records_dic[num].append([timeToMinutes(time), history])
        else:
            records_dic[num] = [[timeToMinutes(time), history]]

    sorted_records = list(records_dic.items())
    sorted_records.sort(key=lambda x: x[0])
    
    for r in sorted_records:
        t = 0
        for info in r[1]:
            if info[1] == 'IN':
                t -= info[0]
            else:
                t += info[0]
        if r[-1][-1][-1] == 'IN':
            t += timeToMinutes('23:59')
        
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt)/ut) * uf)
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", 
           "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)