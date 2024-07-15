# N=2**a x 3**b x 5**c x 7**d x 11**e
# 소인수분해

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # Initialize counters for each prime factor
    a, b, c, d, e = 0, 0, 0, 0, 0

    # Count the factors of 2
    while N % 2 == 0:
        a += 1
        N //= 2
    
    # Count the factors of 3
    while N % 3 == 0:
        b += 1
        N //= 3

    # Count the factors of 5
    while N % 5 == 0:
        c += 1
        N //= 5

    # Count the factors of 7
    while N % 7 == 0:
        d += 1
        N //= 7

    # Count the factors of 11
    while N % 11 == 0:
        e += 1
        N //= 11

    print(f"#{test_case} {a} {b} {c} {d} {e}")

