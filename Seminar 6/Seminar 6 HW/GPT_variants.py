# Вариант с рекурсией
# def is_valid(board, row, col):
#     for i in range(row):
#         if board[i] == col or board[i] - col == row - i or board[i] - col == i - row:
#             return False
#     return True
#
# def solve(board, row, solutions):
#     if row == len(board):
#         solutions.append(list(board))
#     else:
#         for col in range(len(board)):
#             if is_valid(board, row, col):
#                 board[row] = col
#                 solve(board, row+1, solutions)
#
# def find_all_solutions():
#     board = [-1] * 8
#     solutions = []
#     solve(board, 0, solutions)
#     return solutions
#
# solutions = find_all_solutions()
# for solution in solutions:
#     print(solution)

# Вариант без рекурсии
# def is_valid(board, row, col):
#     for i in range(row):
#         if board[i] == col or board[i] - col == row - i or board[i] - col == i - row:
#             return False
#     return True
#
# def find_all_solutions():
#     board = [-1] * 8
#     solutions = []
#     row = 0
#     while row >= 0:
#         if row == 8:
#             solutions.append(list(board))
#             row -= 1
#         elif board[row] == 7:
#             board[row] = -1
#             row -= 1
#         else:
#             board[row] += 1
#             if is_valid(board, row, board[row]):
#                 row += 1
#     return solutions
#
# solutions = find_all_solutions()
# for solution in solutions:
#     print(solution)