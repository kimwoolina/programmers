# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())

    # 방법 1
    # result = 0
    # for i in range(1, num + 1):
    #     if i % 2 == 0:
    #         result -= i
    #     else:
    #         result += i
    

    #방법 2

    # 홀수의 합 구하기
    odd_sum = ((num + 1) // 2) ** 2
    
    # 짝수의 합 구하기
    even_sum = (num // 2) * (num // 2 + 1)
    
    # 결과는 홀수의 합에서 짝수의 합을 뺀 값
    result = odd_sum - even_sum
    
    print(f"#{test_case} {result}")