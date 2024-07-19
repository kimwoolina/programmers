# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

import math

def calculate_gcd_lcm(a, b):
    # Calculate GCD(최대공약수)
    gcd = math.gcd(a, b)
    
    # Calculate LCM(최소공배수)
    lcm = (a * b) // gcd
    
    # Return as a list
    return [gcd, lcm]

n, m = map(int, input().strip().split(' '))

result = calculate_gcd_lcm(n, m)
print(result)

# 다른 방법
def gcdlcm1(a, b):
    c,d = max(a, b), min(a, b)
    t = 1
    while t>0:
        t = c%d
        c, d = d, t
    answer = [ c, int (a*b/c)]
    return answer

def gcdlcm2(a, b):
    for i in range(a):
        if a%(a-i)+b%(a-i) == 0:
            return [a-i, a*b/(a-i)]