def solution(a, b, n):
    answer = 0
    while n >= a:
        n-=a
        n+=b
        answer+=b
    return answer

#test
print(solution(2,1,20)) # 19
print(solution(3,1,20)) # 9