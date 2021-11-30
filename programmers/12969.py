# 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

for x in range(b):
    tmp = ""
    for y in range(a):
        tmp += '*'
    print(tmp)
