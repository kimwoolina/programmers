# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
# F(n) = F(n-1) + F(n-2) 

def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    result = ( solution(n-1) + solution(n-2) ) % 1234567
    return result


print(solution(3))
print(solution(5))
