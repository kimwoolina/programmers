# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
# F(n) = F(n-1) + F(n-2) 

def solution(n):
    MOD = 1234567

    a, b = 0, 1
    
    # n이 2 이상이라는 제약이 있으므로, 반복문을 2부터 n까지 실행
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    
    return b

# test
print(solution(3))  # 2
print(solution(5))  # 5
