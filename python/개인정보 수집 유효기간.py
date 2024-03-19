def parse_date(date_str):
    return tuple(map(int, date_str.split('.')))

def compare_dates(date1, date2):
    return date1 <= date2

def solution(today, terms, privacies):
    today = parse_date(today)
    answer = []

    for index, pr in enumerate(privacies, 1):
        pr_date = parse_date(pr[:10])
        for t in terms:
            if t.split()[0] in pr:
                year_plus = int(t.split()[1]) // 12
                month_plus = int(t.split()[1]) % 12
                new_year = int(pr[0:4]) + year_plus
                new_month = pr_date[1] + month_plus
                if new_month > 12:
                    new_year += 1
                    new_month -= 12
                new_date = (new_year, new_month, pr_date[2])
                if compare_dates(new_date, today):
                    answer.append(index)
                    break
    return answer


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

solution(today, terms, privacies)