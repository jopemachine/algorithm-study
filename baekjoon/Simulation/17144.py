'''
==============================================================================================
@ Title: 미세먼지 안녕!
@ URL: https://www.acmicpc.net/problem/17144
@ Author: jopemachine
@ Created Date: 10/1/2022, 9:42:12 AM
@ Description:
미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인
격자판으로 나타냈고, 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을
실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다. 공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두
행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다. 1초 동안
아래 적힌 일이 순서대로 일어난다. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다. (r, c)에 있는
미세먼지는 인접한 네 방향으로 확산된다. 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
확산되는 양은 Ar,c/5이고 소수점은 버린다. (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수)
이다. 공기청정기가 작동한다. 공기청정기에서는 바람이 나온다. 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의
바람은 시계방향으로 순환한다. 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다. 공기청정기에서 부는 바람은 미세먼지가
없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다. 다음은 확산의 예시이다. 왼쪽과 오른쪽에 칸이 없기 때문에, 두
방향으로만 확산이 일어났다. 인접한 네 방향으로 모두 확산이 일어난다. 공기청정기가 있는 칸으로는 확산이 일어나지 않는다. 공기청정기의
바람은 다음과 같은 방향으로 순환한다. 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.
@ Input: 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다. 둘째 줄부터 R개의 줄에 Ar,c (-1
≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번
위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
@ Output: 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
@ Ref: https://unie2.tistory.com/942
==============================================================================================
'''
R, C, T = map(int, input().split())
_map = list(list(map(int, input().split())) for _ in range(R))

air_purifier_pos = []

for i in range(R):
  if _map[i][0] == -1:
    air_purifier_pos.append((i, 0))
    air_purifier_pos.append((i + 1, 0))
    break

up_dr = [0, -1, 0, 1]
up_dc = [1, 0, -1, 0]

down_dr = [0, 1, 0, -1]
down_dc = [1, 0, -1, 0]

for _ in range(T):
  spreading_map = [[0] * C for _ in range(R)]

  # print(_map)

  # 확산
  for i in range(R):
    for j in range(C):
      if _map[i][j] != 0 and _map[i][j] != -1:
        amount = _map[i][j] // 5
        cnt = 0

        for k in range(4):
          nr = i + up_dr[k]
          nc = j + up_dc[k]
          if 0 <= nr < R and 0 <= nc < C and _map[nr][nc] != -1:
            spreading_map[nr][nc] += amount
            cnt += 1

        _map[i][j] -= amount * cnt

  for i in range(R):
    for j in range(C):
      _map[i][j] += spreading_map[i][j]

  # up
  dir = 0
  before = 0

  r, c = air_purifier_pos[0]
  c += 1

  while True:
    if r == air_purifier_pos[0][0] and c == 0:
      break

    nr = r + up_dr[dir]
    nc = c + up_dc[dir]

    if not 0 <= nr < R or not 0 <= nc < C:
      dir += 1
      continue

    _map[r][c], before = before, _map[r][c]
    r, c = nr, nc

  # down
  dir = 0
  before = 0

  r, c = air_purifier_pos[1]
  c += 1

  while True:
    if r == air_purifier_pos[1][0] and c == 0:
      break

    nr = r + down_dr[dir]
    nc = c + down_dc[dir]

    if not 0 <= nr < R or not 0 <= nc < C:
      dir += 1
      continue

    _map[r][c], before = before, _map[r][c]
    r, c = nr, nc

sum = 0
for i in range(R):
  for j in range(C):
    if _map[i][j] > 0:
      sum += _map[i][j]

print(sum)