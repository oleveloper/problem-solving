# 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    arr = [[0 for col in range(columns)] for row in range(rows)]
    i = 1
    for row in range(rows):
        for col in range(columns):
            arr[row][col] = i
            i += 1
    
    for x1, y1, x2, y2 in queries:
        start = arr[x1 - 1][y1 - 1]
        m = start
        
        for n in range(x1 - 1, x2 - 1):
            test = arr[n + 1][y1 - 1]
            arr[n][y1 - 1] = test
            m = min(m, test)

        for n in range(y1 - 1, y2 - 1):
            test = arr[x2 - 1][n + 1]
            arr[x2 - 1][n] = test
            m = min(m, test)

        for n in range(x2 - 1,x1 - 1, -1):
            test = arr[n - 1][y2 - 1]
            arr[n][y2 - 1] = test
            m = min(m, test)

        for n in range(y2 - 1,y1 - 1, -1):
            test = arr[x1 - 1][n - 1]
            arr[x1 - 1][n] = test
            m = min(m, test)
        
        arr[x1 - 1][y1] = start
        answer.append(m)
            
    return answer
