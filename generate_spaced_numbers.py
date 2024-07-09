# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.

def solution(x, n):
    return [x * i for i in range(1, n + 1)]

# 예시 테스트
print(solution(2, 5))  # 출력: [2, 4, 6, 8, 10]
print(solution(4, 3))  # 출력: [4, 8, 12]
print(solution(-4, 2)) # 출력: [-4, -8]
