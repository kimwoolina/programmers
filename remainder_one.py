#나머지가 1이 되는 수  찾기

# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1,000,000

def remainder_one(n):
    for x in range(2, n): # x는 n보다 작아야하며 최소 1 이상이므로 x=2 이상
        if n % x == 1:
            return x
        
#test
print(remainder_one(10))
print(remainder_one(12))