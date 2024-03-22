def solution(today, terms, privacies):
    answer = []
    for i, pr in enumerate(privacies, 1):
        for t in terms:
            if t.split()[0] in pr:
                year_plus = (int(t.split()[1])) // 12
                month_plus = (int(t.split()[1])) % 12
                new_year = int(pr[0:4]) + year_plus
                new_month = int(pr[5:7]) + month_plus   
                if new_month > 12:
                    new_year += 1
                    new_month -= 12
                if len(str(new_month)) == 1:
                    new_month = '0' + str(new_month)
                new_date = str(new_year) + '.' + str(new_month) + '.' + pr[8:10]
                print(new_date)
                if new_date <= today:
                    answer.append(i)
                    break
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(today, terms, privacies)