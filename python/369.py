def game_369(x):
    for i in range(1, x+1):
        cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')

        if cnt > 0:
            print('X' * cnt, end = ' ')
        else:
            print(i, end=' ')

game_369(40)