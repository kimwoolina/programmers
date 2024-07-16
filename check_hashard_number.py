def solution(n):
    return n%sum(int(x) for x in str(n)) == 0

n = int(input())
print(solution(n))