# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 리턴
# 만약 처음 나온 글자라면 -1로 표현
# s="banana"라고 할 때, 

def solution(s):
    answer =[]
    my_dict = {}

    for i in range(len(s)):

        if s[i] in my_dict:
            answer.append(i - my_dict[s[i]])
            my_dict[s[i]] = i
        else:
            my_dict[s[i]] = i
            answer.append(-1)

    return answer

print(solution("banana")) #[-1, -1, -1, 2, 2, 2]
print(solution("foobar")) #[-1, -1, 1, -1, -1, -1]

