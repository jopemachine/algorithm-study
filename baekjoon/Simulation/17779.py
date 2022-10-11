'''
==============================================================================================
@ Title: 게리맨더링 2
@ URL: https://www.acmicpc.net/problem/17779
@ Author: jopemachine
@ Created Date: 10/7/2022, 10:29:46 AM
@ Description:
재현시의 시장 구재현은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진
구재현은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 재현시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고
한다. 재현시는 크기가 N×N인 격자로 나타낼 수 있다. 격자의 각 칸은 구역을 의미하고, r행 c열에 있는 구역은 (r, c)로
나타낼 수 있다. 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도
하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수
있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야
한다. 선거구를 나누는 방법은 다음과 같다. 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x
< x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N) 다음 칸은 경계선이다. (x, y), (x+1, y-1),
..., (x+d1, y-d1) (x, y), (x+1, y+1), ..., (x+d2, y+d2) (x+d1, y-d1),
(x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2) (x+d2, y+d2), (x+d2+1, y+d2-1),
..., (x+d2+d1, y+d2-d1) 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다. 5번 선거구에 포함되지 않은 구역
(r, c)의 선거구 번호는 다음 기준을 따른다. 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y 2번 선거구: 1 ≤ r ≤
x+d2, y < c ≤ N 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2 4번 선거구: x+d2 < r ≤ N,
y-d1+d2 ≤ c ≤ N 아래는 크기가 7×7인 재현시를 다섯 개의 선거구로 나눈 방법의 예시이다. x = 2, y = 4, d1
= 2, d2 = 2 x = 2, y = 5, d1 = 3, d2 = 2 x = 4, y = 3, d1 = 1, d2 = 1 구역
(r, c)의 인구는 A[r][c]이고, 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값이다. 선거구를 나누는 방법
중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.
@ Input: 첫째 줄에 재현시의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에 N개의 정수가 주어진다. r행 c열의 정수는 A[r][c]를
의미한다.
@ Output: 첫째 줄에 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 출력한다.
@ Ref: https://jjangsungwon.tistory.com/69
==============================================================================================
'''

import math

N = int(input())
_map = [list(map(int, input().split())) for _ in range(N)]

map_sum = sum(map(sum, _map))

# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값
min_diff = math.inf

for x in range(1, N + 1):
  for y in range(1, N + 1):
    for d1 in range(1, N + 1):
      for d2 in range(1, N + 1):
        if not (1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N):
          continue

        selection = [[0] * (N + 1) for _ in range(N + 1)]

        # 1번 경계선
        for k in range(0, d1 + 1):
          selection[x + k][y - k] = 5

        # 2번 경계선
        for k in range(0, d2 + 1):
          selection[x + k][y + k] = 5

        # 3번 경계선
        for k in range(0, d2 + 1):
          selection[x + d1 + k][y - d1 + k] = 5

        # 4번 경계선
        for k in range(0, d1 + 1):
          selection[x + d2 + k][y + d2 - k] = 5

        # 각 선거구의 인구 합
        sums = [0, 0, 0, 0, 0]

        # 1번 선거구
        for r in range(1, x + d1):
          for c in range(1, y + 1):
            if selection[r][c] == 5:
              break

            selection[r][c] = 1
            sums[0] += _map[r - 1][c - 1]

        # 2번 선거구
        for r in range(1, x + d2 + 1):
          for c in range(N, y, -1):
            if selection[r][c] == 5:
              break

            selection[r][c] = 2
            sums[1] += _map[r - 1][c - 1]

        # 3번 선거구
        for r in range(x + d1, N + 1):
          for c in range(1, y - d1 + d2):
            if selection[r][c] == 5:
              break

            selection[r][c] = 3
            sums[2] += _map[r - 1][c - 1]

        # 4번 선거구
        for r in range(x + d2 + 1, N + 1):
          for c in range(N, y - d1 + d2 - 1, -1):
            if selection[r][c] == 5:
              break

            selection[r][c] = 4
            sums[3] += _map[r - 1][c - 1]

        # 경계 내부의 계산 못한 5번 선거구 인구의 합은 다른 선거구 인구 합으로 계산하면 된다.
        sums[4] = map_sum - sum(sums[:4])
        min_diff = min(max(sums) - min(sums), min_diff)
        # print(sums)

print(min_diff)
