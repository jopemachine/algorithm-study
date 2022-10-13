'''
==============================================================================================
@ Title: 캐슬 디펜스
@ URL: https://www.acmicpc.net/problem/17135
@ Author: jopemachine
@ Created Date: 10/13/2022, 12:36:04 PM
@ Description:
캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다. 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다.
격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다. 격자판의 N번행의 바로 아래(N+1번 행)의
모든 칸에는 성이 있다. 성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다. 궁수는 성이 있는 칸에 배치할 수 있고, 하나의
칸에는 최대 1명의 궁수만 있을 수 있다. 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다. 궁수가
공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다. 같은 적이
여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다. 적은 아래로 한 칸
이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다.  게임 설명에서 보다시피
궁수를 배치한 이후의 게임 진행은 정해져있다. 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의
공격으로 제거할 수 있는 적의 최대 수를 계산해보자. 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| +
|c1-c2|이다.
@ Input: 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다. 둘째 줄부터 N개의 줄에는 격자판의 상태가
주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.
@ Output: 첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.
==============================================================================================
'''
from queue import deque
from copy import deepcopy

N, M, D = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]
original_map = deepcopy(_map)
max_res = 0

# 왼쪽 방향에서 시작해 시계 방향으로 순회
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def move_monster():
  # 마지막 줄의 경우 그냥 몬스터들을 게임에서 제외
  for c in range(M):
    if _map[N - 1][c] == 1:
      _map[N - 1][c] = 0

  for r in range(N - 1, 0, -1):
    for c in range(M):
      # 윗 줄에 몬스터가 있다면 아래로 내림.
      if _map[r - 1][c] == 1:
        _map[r][c], _map[r - 1][c] = 1, 0

def check_monster_exist():
  for r in range(N):
    for c in range(M):
      if _map[r][c] == 1:
        return True
  return False

# 궁수가 쏠 수 있는, 가장 가까운 몬스터의 위치 및 거리를 반환
def get_min_dist(r, c):
  que = deque([(r, c, 1)])

  visited = [[False] * M for _ in range(N)]

  while que:
    r, c, dist = que.popleft()
    visited[r][c] = True

    # 몬스터 발견하는 즉시 반환
    if _map[r][c] == 1:
      return (r, c, dist)

    for k in range(len(dr)):
      nr = r + dr[k]
      nc = c + dc[k]
      if 0 <= nr < N and 0 <= nc < M:
        if not visited[nr][nc] and dist < D:
          que.append((nr, nc, dist + 1))

  # 가시거리에 몬스터가 없음
  return None

# 궁수 3명의 위치가 결정되면 총 잡을 몬스터의 수가 결정된다.
for x1 in range(M):
  for x2 in range(x1 + 1, M):
    for x3 in range(x2 + 1, M):
      res = 0
      _map = deepcopy(original_map)

      # 몬스터가 1마리 이상 존재하는지 확인
      while check_monster_exist():
        # print(_map)

        # 각 궁수들간 가장 가까운 거리의 몬스터 위치 계산
        res1 = get_min_dist(N - 1, x1)
        res2 = get_min_dist(N - 1, x2)
        res3 = get_min_dist(N - 1, x3)

        # 각 위치들은 중복될 수 있다.
        removed = set()

        # 결정된 위치의 몬스터들은 제거
        if res1:
          m1_r, m1_c, m1_d = res1
          _map[m1_r][m1_c] = 0
          removed.add((m1_r, m1_c))

        if res2:
          m2_r, m2_c, m2_d = res2
          _map[m2_r][m2_c] = 0
          removed.add((m2_r, m2_c))

        if res3:
          m3_r, m3_c, m3_d = res3
          _map[m3_r][m3_c] = 0
          removed.add((m3_r, m3_c))
        # print(removed)

        # 제거된 몬스터의 마릿 수 만큼 카운트
        res += len(removed)

        # 몬스터 움직임
        move_monster()

      max_res = max(res, max_res)

print(max_res)
