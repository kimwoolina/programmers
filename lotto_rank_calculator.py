# 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 
# 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
# 알아볼 수 없는 번호를 0으로 표기합니다.
# 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.

def solution(lottos, win_nums):
    set1 = set(lottos)
    set2 = set(win_nums)
    
    cnt_zero = lottos.count(0)
    
    intersection = len(set(set1 & set2)) + cnt_zero
    difference = len(set2.intersection(set1)) 
    
    rank_dict = {6:1, 5:2, 4:3, 3:4, 2:5}
    
    answer1 = rank_dict[intersection] if intersection in rank_dict else 6
    answer2 = rank_dict[difference] if difference in rank_dict else 6
    
    return [answer1, answer2]