'''
==============================================================================================
@ Title: 인구 이동
@ URL: https://www.acmicpc.net/problem/16234
@ Author: jopemachine
@ Created Date: 9/30/2022, 2:41:12 PM
@ Description:
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는
A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형
형태이다. 오늘부터 인구 이동이 시작되는 날이다. 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이
없을 때까지 지속된다. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루
동안 연다. 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다. 국경선이 열려있어 인접한 칸만을 이용해 이동할
수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고
있는 칸의 개수)가 된다. 편의상 소수점은 버린다. 연합을 해체하고, 모든 국경선을 닫는다. 각 나라의 인구수가 주어졌을 때, 인구
이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100) 둘째 줄부터 N개의 줄에 각 나라의 인구수가
주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100) 인구 이동이 발생하는 일수가
2,000번 보다 작거나 같은 입력만 주어진다.
@ Output: 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
==============================================================================================
'''
from collections import deque
from functools import reduce
from math import trunc

N, L, R = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

res = 0

while True:
  visited = [[False for _ in range(N)] for _ in range(N)]
  should_next = False

  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        que = deque([(i, j)])
        visited[i][j] = True
        visited_pts = [(i, j)]

        while que:
          r, c = que.popleft()

          for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= N or nc >= N or nr < 0 or nc < 0:
              continue

            if not visited[nr][nc] and L <= abs(_map[nr][nc] - _map[r][c]) <= R:
              visited[nr][nc] = True
              should_next = True
              que.append((nr, nc))
              visited_pts.append((nr, nc))

        avg = trunc(reduce(lambda acc, cur: acc + _map[cur[0]][cur[1]], visited_pts, 0) / len(visited_pts))

        for r, c in visited_pts:
          _map[r][c] = avg

  if not should_next:
    break

  res += 1

print(res)