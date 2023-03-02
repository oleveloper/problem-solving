# 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    xlen, ylen = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = 999, 999, -1, -1
    
    for x in range(xlen):
        for y in range(ylen):
            if wallpaper[x][y] == '#':
                lux, luy = min(lux, x), min(luy, y)
                rdx, rdy = max(rdx, x), max(rdy, y)
    
    return [lux, luy, rdx + 1, rdy + 1]
