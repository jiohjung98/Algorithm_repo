def day_calc(x,y):
    if y == 2:
        if x % 4 == 0:
            if x % 100 == 0:
                return 28
            elif x % 100 == 0 and x % 400 == 0:
                return 29
            else:
                return 29
        else:
            return 28
    if y == 4 or y == 6 or y == 9 or y == 11:
        return 30
    else:
        return 31

def season_calc(x,y,z):
    maxDay = day_calc(x,y)
    if maxDay < z:
        print(-1)
    else:
        if y <= 3:
            print('Spring')
        elif 3 < y and y <= 6:
            print('Summer')
        elif 6 < y and y <= 9:
            print('Fall')
        else:
            print('Winter')

y, m, d = map(int, input().split())

season_calc(y,m,d)