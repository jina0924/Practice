# 백준 18428번 감시피하기

import sys
sys.stdin = open('input2.txt')


def check():
    global ans

    for t in teachers:
        cr, cc = t                      # 선생님의 현재 위치
        d = 0                           # 상하좌우를 살펴볼 인덱스값
        while d < 4:                    # 한 선생님이 상하좌우를 모두 살펴볼 때까지 반복
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if data[nr][nc] == 'S': # 선생님과 학생이 바로 인접해있다면 더 볼것도 없이 'NO'
                    return
                elif data[nr][nc] == 'O':   # 장애물이라면 다른 방향 살피러 감
                    d += 1
                    cr, cc = t          # 원래 선생님 위치로 원상복귀
                else:                   # 아무것도 없거나 다른 선생님이라면
                    cr, cc = nr, nc     # 새 위치를 저장하고 그 다음 위치 살피러 감
            else:                       # 새로 본 위치가 범위를 벗어났다면 다른 방향 살펴봄
                d += 1
                cr, cc = t
    ans = 'YES'                         # 반복문에서 return을 만나지 않았다 = 학생을 본 적 없다 = 감시 피하기 성공


def hide(cnt):
    if cnt >= 3:                        # 장애물 3개 설치했으면 모두 감시 피할 수 있는지 확인하기
        check()
        return
    for r in range(N):
        for c in range(N):
            if data[r][c] == 'X':       # 장애물 설치하기
                data[r][c] = 'O'
                hide(cnt + 1)
                data[r][c] = 'X'        # 장애물 설치했던 위치 되돌리기


N = int(input())
data = []                               # 복도 정보 담을 리스트
teachers = []                           # 선생님 위치 정보를 담을 리스트
for r in range(N):
    row = list(input().split())
    data.append(row)
    for c in range(N):
        if row[c] == 'T':               # 선생님이면 해당 위치를 저장해둠
            teachers.append((r, c))
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)   # 상하좌우
ans = 'NO'                              # 모든 학생이 감시를 피할 수 있으면 ans값을 'YES'로 바꿀 예정
hide(0)                                 # 장애물 설치하러 감
print(ans)