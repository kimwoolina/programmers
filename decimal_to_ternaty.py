# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

from collections import deque

def solution(n):
    n = ''.join(reversed(decimal_to_ternary(n)))  # 문자열로 변환하여 뒤집음
    return ternary_to_decimal(n)

# 10 진법 -> 3진법
def decimal_to_ternary(decimal):
    q = deque([])
    
    if decimal == 0:
        q.appendleft(0)
    
    while decimal > 0:
        q.appendleft(decimal % 3)
        decimal //= 3
    
    return ''.join(map(str, q))  # 리스트를 문자열로 변환하여 반환
    
# 3진법 -> 10진법
def ternary_to_decimal(ternary_str):
    decimal_value = 0
    length = len(ternary_str)
    
    for i in range(length):
        digit = int(ternary_str[length - i - 1])
        decimal_value += digit * (3 ** i)
    
    return decimal_value



# 매우 간단한, 방법 2
def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

# 테스트 케이스
print(solution(45))  # 출력: 7
print(solution(125))  # 출력: 229
