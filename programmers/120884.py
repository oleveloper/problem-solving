# 치킨 쿠폰
# https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    answer = 0
    coupon = chicken
    
    while chicken > 0:
        chicken, coupon = divmod(coupon, 10)
        answer += chicken
        coupon += chicken
        
    return answer
