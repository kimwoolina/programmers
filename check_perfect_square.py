# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

import math

def solution(n):
    answer = 0
    # n ** 1/2 도 할 수 있다.
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        answer = (sqrt_n + 1)**2
    else:
        answer = -1
        
    return answer