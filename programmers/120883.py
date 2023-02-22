# 로그인 성공?
# https://school.programmers.co.kr/learn/courses/30/lessons/120883

def solution(id_pw, db):
    id, pw = id_pw[0], id_pw[1]
    
    for dbid, dbpw in db:
        if dbid == id:
            if dbpw == pw:
                return "login"
            else:
                return "wrong pw"
    
    return "fail"
