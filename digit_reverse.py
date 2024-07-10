# 자연수 뒤집어 배열로 만들기

def solution(n):
    reverse_num = []
    n = str(n)
    for i in range(1,len(n)+1):
        add_num = int(n[-i])
        reverse_num.append(add_num)
    
    return reverse_num

print(solution(12345))

# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))