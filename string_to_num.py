# 문자열 s를 숫자로 변환한 결과를 반환하는 함수

def solution(s):
    # 문자열이 음수로 시작하면 양수로 변환하고, 그렇지 않으면 그대로 변환
    if s[0] == '-':
        answer = -int(s[1:])
    else:
        answer = int(s)
        
    return answer

s = input("Enter a number: ")

print(solution(s))

# test
print(solution(1234))
print(solution(-1234))