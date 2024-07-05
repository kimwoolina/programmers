# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

n = int(input("정수를 입력하세요: "))
divisors = find_divisors(n)
sum_of_divisors = sum(divisors)
print(f"{n}의 약수의 합: {sum_of_divisors}")
