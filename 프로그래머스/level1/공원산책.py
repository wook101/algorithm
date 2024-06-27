def solution(park, routes):
    x, y = 0, 0
    park = [list(p) for p in park]
    h, w = len(park), len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    for r in routes:
        op, n = r.split(' ')
        n = int(n)
        if op == 'E':
            if 0 <= y + n < w:
                chk = True
                for i in range(1, n + 1):
                    if park[x][y + i] == 'X':
                        chk = False
                if chk:
                    y += n
        elif op == 'W':
            if 0 <= y - n < w:
                chk = True
                for i in range(1, n + 1):
                    if park[x][y - i] == 'X':
                        chk = False
                if chk:
                    y -= n
        elif op == 'S':
            if 0 <= x + n < h:
                chk = True
                for i in range(1, n + 1):
                    if park[x + i][y] == 'X':
                        chk = False
                if chk:
                    x += n
        else:
            if 0 <= x - n < h:
                chk = True
                for i in range(1, n + 1):
                    if park[x - i][y] == 'X':
                        chk = False
                if chk:
                    x -= n
    return [x, y]