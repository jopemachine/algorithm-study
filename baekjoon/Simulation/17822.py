'''
==============================================================================================
@ Title: 원판 돌리기
@ URL: https://www.acmicpc.net/problem/17822
@ Author: jopemachine
@ Created Date: 10/18/2022, 6:47:15 PM
@ Level: Gold 3
@ Description:
반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i이면,
그 원판을 i번째 원판이라고 한다. 각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로
표현한다. 수의 위치는 다음을 만족한다. (i, 1)은 (i, 2), (i, M)과 인접하다. (i, M)은 (i, M-1), (i,
1)과 인접하다. (i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1) (1, j)는 (2, j)와
인접하다. (N, j)는 (N-1, j)와 인접하다. (i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤
N-1) 아래 그림은 N = 3, M = 4인 경우이다. 원판의 회전은 독립적으로 이루어진다. 2번 원판을 회전했을 때, 나머지 원판은
회전하지 않는다. 원판을 회전시킬 때는 수의 위치를 기준으로 하며, 회전시킨 후의 수의 위치는 회전시키기 전과 일치해야 한다. 다음
그림은 원판을 회전시킨 예시이다. 1번 원판을 시계 방향으로 1칸 회전 2, 3번 원판을 반시계 방향으로 3칸 회전 1, 3번 원판을
시계 방향으로 2칸 회전 원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째
회전할때 사용하는 변수는 xi, di, ki이다. 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계
방향, 1인 경우는 반시계 방향이다. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다. 그러한 수가 있는
경우에는 원판에서 인접하면서 같은 수를 모두 지운다. 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고,
작은 수에는 1을 더한다. 원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.
@ Input: 첫째 줄에 N, M, T이 주어진다. 둘째 줄부터 N개의 줄에 원판에 적힌 수가 주어진다. i번째 줄의 j번째 수는 (i, j)에 적힌
수를 의미한다. 다음 T개의 줄에 xi, di, ki가 주어진다.
@ Output: 원판을 T번 회전시킨 후 원판에 적힌 수의 합을 출력한다.
==============================================================================================
'''

from collections import deque
from math import inf

N, M, T = map(int, input().split())
nums = list(deque(map(int, input().split())) for _ in range(N))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# T번 원판을 돌린다.
for t in range(T):
  x, d, k = map(int, input().split())

  # 각 원판의 번호가 x의 배수인지 확인해 k번 만큼 돌림
  for i in range(N):
    if (i + 1) % x == 0:
      nums[i].rotate((1 if d == 0 else -1) * k)

  # 원판에서 서로 인접한 수 들을 모두 찾아 지움
  # 인접한 수 들을 모두 찾는 로직은 이차원 배열에서의 완전탐색으로 구현 가능하다.
  erased = False

  for i in range(N):
    for j in range(M):
      if nums[i][j] == inf:
        continue

      visited = [[False] * M for _ in range(N)]
      visited[i][j] = True

      que = deque([(i, j)])
      should_erase = False
      target_num = nums[i][j]

      while que:
        r, c = que.popleft()

        for k in range(4):
          nr, nc = r + dr[k], c + dc[k]
          # 원판을 만들기 위해 필요한 추가 조건
          if nc == -1:
            nc = M - 1
          elif nc == M:
            nc = 0

          if (0 <= nr < N and 0 <= nc < M):
            if visited[nr][nc]:
              continue
            if nums[nr][nc] != target_num:
              continue

            erased, should_erase = True, True
            visited[nr][nc] = True

            nums[nr][nc] = inf
            que.append((nr, nc))

      if should_erase:
        nums[i][j] = inf

  # 원판들 중 중복된 숫자가 하나도 지워지지 않은 경우
  # 평균 값을 구해 비교해 1을 더하거나 뺀다
  if not erased:
    sum_val = 0
    cnt = 0
    for r in range(N):
      for c in range(M):
        if nums[r][c] != inf:
          sum_val += nums[r][c]
          cnt += 1

    # 모든 숫자가 이미 지워짐
    if cnt == 0:
      break

    mean_val = sum_val / cnt
    for r in range(N):
      for c in range(M):
        if nums[r][c] != inf:
          if nums[r][c] > mean_val:
            nums[r][c] -= 1
          elif nums[r][c] < mean_val:
            nums[r][c] += 1

# print(nums)

res = 0
for r in range(N):
  for c in range(M):
    if nums[r][c] != inf:
      res += nums[r][c]

print(res)