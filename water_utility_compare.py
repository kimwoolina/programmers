T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a_result = P*W
    b_result = Q if W <= R else Q + S * (W - R)
    result = 0

    if a_result > b_result:
        result = b_result
    else:
        result = a_result

    print(f"#{test_case} {result}")

    

