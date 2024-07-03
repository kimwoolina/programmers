# 가위 바위 보 게임 만들기

import random

play_list = ['가위', '바위', '보']

win_cnt = 0
lose_cnt = 0
tie_cnt = 0

while True:
    computer_play = random.choice(play_list)
    user_play = input('가위, 바위, 보 중 하나를 선택하세요 :')

    while user_play not in play_list:
            print("유효한 입력이 아닙니다.")
            user_play = input("가위, 바위, 보 중 하나를 선택하세요: ")

    print(f'사용자: {user_play}, 컴퓨터: {computer_play}')

    if user_play == computer_play:
        print('무승부!')
        tie_cnt += 1
    elif (
        (user_play == '가위' and computer_play == '보') or
        (user_play == '바위' and computer_play == '가위') or
        (user_play == '보' and computer_play == '바위')
    ):
        print('사용자 승리!')
        win_cnt += 1
    else:
        print('컴퓨터 승리!')
        lose_cnt += 1


    restart = input('다시 하시겠습니까? (y/n) : ')
    if restart.lower() != 'y':
        print('게임을 종료합니다.')
        break

print(f'승: {win_cnt} 패: {lose_cnt} 무승부: {tie_cnt}')
