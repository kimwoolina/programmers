# Up Down 게임 만들기

import random

def guess_up_down():
    while True:
        random_num = random.randrange(1, 100)
        num = int(input('숫자를 입력하세요: '))
        cnt = 1

        while num != random_num:
            if num < 1 or num > 100:
                print('유효한 범위 내의 숫자를 입력하세요.')
            else:
                cnt += 1
                if num > random_num:
                    print('다운')
                elif num < random_num:
                    print('업')

            num = int(input('숫자를 입력하세요: '))

        print('맞았습니다!')
        print('시도한 횟수: ', cnt)
        
        restart = input('다시 하시겠습니까? (y/n) : ')
        if restart.lower() != 'y':
            print('게임을 종료합니다.')
            break


# Run the game
guess_up_down()
        