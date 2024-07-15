T = int(input())  # 테스트 케이스의 개수를 입력 받음

# 90도 회전: 원래 행렬의 행과 열을 바꾸고, 새로운 행의 순서를 반대로
def rotate_90(matrix):
    N = len(matrix)
    return [[matrix[N - j - 1][i] for j in range(N)] for i in range(N)]

# 180도 회전: 행렬을 상하 반전시키고, 그 결과를 좌우 반전
def rotate_180(matrix):
    N = len(matrix)
    return [[matrix[N - i - 1][N - j - 1] for j in range(N)] for i in range(N)]

# 270도 회전: 원래 행렬의 행과 열을 바꾸고, 새로운 열의 순서를 반대로
def rotate_270(matrix):
    N = len(matrix)
    return [[matrix[j][N - i - 1] for j in range(N)] for i in range(N)]


for test_case in range(1, T + 1):
    N = int(input())  # N 값 입력 받음 (N x N 행렬이므로)
    matrix = []  # 행렬을 저장할 리스트 초기화

    # N 줄에 걸쳐서 행렬의 각 행을 입력 받음
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    matrix_90 = rotate_90(matrix)
    matrix_180 = rotate_180(matrix)
    matrix_270 = rotate_270(matrix)

    print(f"#{test_case}")
    for i in range(N):
        print(''.join(map(str, matrix_90[i])), ''.join(map(str, matrix_180[i])), ''.join(map(str, matrix_270[i])))

