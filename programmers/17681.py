# [1차] 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer, arr1map, arr2map = [], [], []
    f = "{0:0" + str(n) + "b}"

    for i in range(n):
        arr1map.append(f.format(arr1[i]))
        arr2map.append(f.format(arr2[i]))

    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1map[i][j] == '1' or arr2map[i][j] == '1':
                tmp += '#' 
            else:
                tmp += ' '
        answer.append(tmp)
        
    return answer
