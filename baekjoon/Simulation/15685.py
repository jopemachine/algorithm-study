'''
==============================================================================================
@ Title: 드래곤 커브
@ URL: https://www.acmicpc.net/problem/15685
@ Author: jopemachine
@ Created Date: 9/29/2022, 3:26:33 PM
@ Description:
드래곤 커브는 다음과 같은 세 가지 속성으로 이루어져 있으며, 이차원 좌표 평면 위에서 정의된다. 좌표 평면의 x축은 → 방향,
y축은 ↓ 방향이다. 시작 점 시작 방향 세대 0세대 드래곤 커브는 아래 그림과 같은 길이가 1인 선분이다. 아래 그림은 (0,
0)에서 시작하고, 시작 방향은 오른쪽인 0세대 드래곤 커브이다. 1세대 드래곤 커브는 0세대 드래곤 커브를 끝 점을 기준으로 시계
방향으로 90도 회전시킨 다음 0세대 드래곤 커브의 끝 점에 붙인 것이다. 끝 점이란 시작 점에서 선분을 타고 이동했을 때, 가장 먼
거리에 있는 점을 의미한다. 2세대 드래곤 커브도 1세대를 만든 방법을 이용해서 만들 수 있다. (파란색 선분은 새로 추가된 선분을
나타낸다) 3세대 드래곤 커브도 2세대 드래곤 커브를 이용해 만들 수 있다. 아래 그림은 3세대 드래곤 커브이다. 즉, K(K >
1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것이다.
크기가 100×100인 격자 위에 드래곤 커브가 N개 있다. 이때, 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인
정사각형의 개수를 구하는 프로그램을 작성하시오. 격자의 좌표는 (x, y)로 나타내며, 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만
유효한 좌표이다.
@ Input: 첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다. 드래곤
커브의 정보는 네 정수 x, y, d, g로 이루어져 있다. x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0
≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10) 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤
커브는 서로 겹칠 수 있다. 방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다. 0: x좌표가 증가하는 방향 (→) 1:
y좌표가 감소하는 방향 (↑) 2: x좌표가 감소하는 방향 (←) 3: y좌표가 증가하는 방향 (↓)
@ Output: 첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
==============================================================================================
'''
N = int(input())

inputs = list(list(map(int, input().split())) for _ in range(N))

# 0: right
# 1: up
# 2: left
# 3: down
def rotate(dir):
  return (dir + 1) % 4

res_pts = []

for X, Y, D, G in inputs:
  trails = [D]
  for _ in range(G):
    trails += map(lambda x: rotate(x), reversed(trails))

  pts = [(X, Y)]
  for trail in trails:
    r, c = pts[-1]

    if trail == 0:
      pts.append((r + 1, c))
    elif trail == 1:
      pts.append((r, c - 1))
    elif trail == 2:
      pts.append((r - 1, c))
    elif trail == 3:
      pts.append((r, c + 1))
    else:
      assert(False)

  res_pts += pts
  # print(sorted(pts))

res_pts.sort()

_map = [[False for _ in range(102)] for _ in range(102)]

for r, c in res_pts:
  _map[r][c] = True

ans = 0
for i in range(100):
  for j in range(100):
    if _map[i][j] and _map[i][j + 1] and _map[i + 1][j] and _map[i + 1][j + 1]:
      ans += 1

print(ans)
