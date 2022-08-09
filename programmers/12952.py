# N-Queen
# https://school.programmers.co.kr/learn/courses/30/lessons/12952

answer = 0
board = []

def check(x):
    for i in range(x): 
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i: return False
    return True

def nqueen(x, n):
    if x == n:
        global answer
        answer += 1
    else:
        for i in range(n):
            board[x] = i
            if check(x): nqueen(x + 1, n)

def solution(n):
    global answer
    global board
    board = [0] * n
    nqueen(0, n)

    return answer
