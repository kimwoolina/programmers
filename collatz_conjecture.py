# 방법 1 
# def solution(num):
#     answer = 0
    
#     while(num != 1):
#         if answer > 500:
#             return -1
#         answer += 1
#         if num % 2 ==0:
#             num = num / 2
#         else:
#             num = 3*num + 1
    
#     if num == 1:
#         return answer 

# 방법 2
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1 