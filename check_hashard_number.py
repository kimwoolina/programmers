def solution(x):
    return n%sum(int(x) for x in str(n)) == 0

x = input()
solution(x)