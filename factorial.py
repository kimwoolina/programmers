# import sys
# sys.setrecursionlimit(10**7)

# 재귀함수 사용

def factorial(i):
    if i == 0:
        return 1
    
    result = i * factorial(i-1)
    return result

def solution(n):
    for i in range(1, 3628800):
        if factorial(i) < n:
            pass
        elif factorial(i) > n:
            break
    
    return i-1
            

print(solution(3628800))