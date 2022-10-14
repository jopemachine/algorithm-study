'''
==============================================================================================
@ Title: 낚시왕
@ URL: https://www.acmicpc.net/problem/17143
@ Author: jopemachine
@ Created Date: 10/14/2022, 12:39:38 PM
@ Description:
낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다. 격자판의 각 칸은 (r, c)로 나타낼 수 있다. r은
행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다. 칸에는 상어가 최대 한 마리 들어있을 수 있다.
상어는 크기와 속도를 가지고 있다. 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌
순서대로 일어난다. 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다. 낚시왕이 오른쪽으로 한 칸 이동한다. 낚시왕이 있는
열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다. 상어가 이동한다. 상어는
입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다. 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로
바꿔서 속력을 유지한채로 이동한다. 왼쪽 그림의 상태에서 1초가 지나면 오른쪽 상태가 된다. 상어가 보고 있는 방향이 속도의 방향,
왼쪽 아래에 적힌 정수는 속력이다. 왼쪽 위에 상어를 구분하기 위해 문자를 적었다. 상어가 이동을 마친 후에 한 칸에 상어가 두 마리
이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다. 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을
때, 낚시왕이 잡은 상어 크기의 합을 구해보자.
@ Input: 첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C) 둘째 줄부터 M개의
줄에 상어의 정보가 주어진다. 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤
1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. (r, c)는 상어의 위치, s는 속력, d는 이동 방향,
z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다. 두 상어가 같은 크기를
갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
@ Output: 낚시왕이 잡은 상어 크기의 합을 출력한다.
==============================================================================================
'''
from copy import deepcopy

R, C, M = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 속도, 방향, 크기
sharks_map = [[[] for _ in range(C)] for _ in range(R)]

for r, c, s, d, z in list(list(map(int, input().split())) for _ in range(M)):
  sharks_map[r - 1][c - 1].append((s, d - 1, z))

player_col_pos = 0
total_score = 0

def move_shark():
  new_map = [[[] for _ in range(C)] for _ in range(R)]

  # 모든 상어를 이동시킴
  for r in range(R):
    for c in range(C):
      # sharks_map엔 칸 당 한 마리 상어밖에 없음
      if sharks_map[r][c]:
        nr, nc = r, c
        speed, dir, size = sharks_map[r][c][0]
        # 상어를 speed만큼 이동시키는데, 벽에 부딪치면 방향을 튼 후 움직인다.
        for _ in range(speed):
          if not (0 <= nr + dr[dir] < R and 0 <= nc + dc[dir] < C):
            if dir == 0 or dir == 1:
              dir = 1 - dir
            elif dir == 2:
              dir = 3
            elif dir == 3:
              dir = 2

          nr += dr[dir]
          nc += dc[dir]
        new_map[nr][nc].append((speed, dir, size))

  # new_map엔 같은 칸에 여러 상어가 있을 수 있음
  return new_map

while player_col_pos < C:
  # print(player_col_pos)

  # print(sharks_map)

  # 해당 열의 가장 가까운 상어를 잡아들임
  for r in range(R):
    if sharks_map[r][player_col_pos]:
      # 2번째 값이 상어의 크기
      total_score += sharks_map[r][player_col_pos][0][2]
      sharks_map[r][player_col_pos] = []
      break

  # 모든 상어를 이동시킴
  next_sharks_map = move_shark()

  # 같은 칸에 여러 상어가 있는 경우 한 마리만 남기도록 처리
  for r in range(R):
    for c in range(C):
      if len(next_sharks_map[r][c]) >= 2:
        next_sharks_map[r][c] = [sorted(next_sharks_map[r][c], key=lambda shark: -shark[2])[0]]

  sharks_map = deepcopy(next_sharks_map)

  # 플레이어가 오른쪽으로 한 칸 이동
  player_col_pos += 1

print(total_score)