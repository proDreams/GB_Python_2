import time
from random import randint


def check_queen_positions(positions: list):
    board = [['.' for _ in range(8)] for _ in range(8)]
    board[positions[0][0]][positions[0][1]] = 'Q'
    for row, col in positions[1:]:
        if 'Q' in board[row]:
            return False
        elif 'Q' in [i[col] for i in board]:
            return False
        elif 'Q' in [board[i][j] for i in range(8) for j in range(8) if abs(i - row) == abs(j - col)]:
            return False
        board[row][col] = 'Q'
    return positions


def generate_random_positions():
    positions = []
    while len(positions) < 8:
        rand = randint(0, 7), randint(0, 7)
        if rand not in positions:
            positions.append(rand)
    return positions


def generate_all():
    success = []
    start_time = time.time()
    numbers_a = [i for i in range(8)]
    for a in numbers_a:
        variants = [(0, a)]
        numbers_b = numbers_a[:]
        numbers_b.remove(a)
        for b in numbers_b:
            variants = [(0, a), (1, b)]
            if check_queen_positions(variants):
                numbers_c = numbers_b[:]
                numbers_c.remove(b)
                for c in numbers_c:
                    variants = [(0, a), (1, b), (2, c)]
                    if check_queen_positions(variants):
                        numbers_d = numbers_c[:]
                        numbers_d.remove(c)
                        for d in numbers_d:
                            variants = [(0, a), (1, b), (2, c), (3, d)]
                            if check_queen_positions(variants):
                                numbers_e = numbers_d[:]
                                numbers_e.remove(d)
                                for e in numbers_e:
                                    variants = [(0, a), (1, b), (2, c), (3, d), (4, e)]
                                    if check_queen_positions(variants):
                                        numbers_f = numbers_e[:]
                                        numbers_f.remove(e)
                                        for f in numbers_f:
                                            variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f)]
                                            if check_queen_positions(variants):
                                                numbers_g = numbers_f[:]
                                                numbers_g.remove(f)
                                                for g in numbers_g:
                                                    variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f), (6, g)]
                                                    if check_queen_positions(variants):
                                                        numbers_h = numbers_g[:]
                                                        numbers_h.remove(g)
                                                        for h in numbers_h:
                                                            variants = [(0, a), (1, b), (2, c), (3, d), (4, e), (5, f),
                                                                        (6, g), (7, h)]
                                                            if check_queen_positions(variants):
                                                                success.append(variants)
    print("--- %s seconds ---" % (time.time() - start_time))
    return success
