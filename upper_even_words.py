def solution(n):
    words = n.split()
    answer = []
    
    for word in words:
        upper_words = []
        for i in range(len(word)):
            if i % 2 == 0:
                upper_words.append(word[i].upper())
            else:
                upper_words.append(word[i].lower())
        answer.append(''.join(upper_words))
    
    return ' '.join(answer)

print(solution("try hello world"))