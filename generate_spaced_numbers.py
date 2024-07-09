# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.

def solution(x, n):
    return [x * i for i in range(1, n+1)]

if __name__ == "__main__":
    x = int(input("간격을 입력하세요 (x): "))
    n = int(input("생성할 숫자의 개수를 입력하세요 (n): "))

    result = solution(x, n)
    print(result)