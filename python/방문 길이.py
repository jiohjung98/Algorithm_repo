def solution(dirs):
    dir = {'U': (1,0), 'D': (-1,0), 'R': (0,1), 'L': (0,-1)}
    sets = set()
    y, x = 0, 0
    
    for d in dirs:
        dy, dx = dir[d]
        ny = y + dy
        nx = x + dx
        
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            sets.add(((y,x), (ny, nx)))
            sets.add(((ny,nx), (y,x)))
            y, x = ny, nx
    return len(sets) // 2
