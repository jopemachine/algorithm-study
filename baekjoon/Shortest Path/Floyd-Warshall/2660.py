'''
==============================================================================================
@ Title: 회장뽑기
@ URL: https://www.acmicpc.net/problem/2660
@ Author: jopemachine
@ Created Date: 10/9/2022, 10:38:36 AM
@ Description:
월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는
사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다. 예를 들어
어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의
친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.
4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의
친구사이이면, 이 두사람은 친구사이라고 본다. 회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는
모든 사람을 찾는 프로그램을 작성하시오.
@ Input: 입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데,
이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.
@ Output: 첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.
==============================================================================================
'''

import math

N = int(input())

dp = [[math.inf for _ in range(N)] for _ in range(N)]

for i in range(N):
  dp[i][i] = 0

while True:
  l, r = map(int, input().split())
  if l == -1 and r == -1:
    break
  l -= 1
  r -= 1

  dp[l][r] = 1
  dp[r][l] = 1

for k in range(N):
  for i in range(N):
    if dp[i][k] == math.inf or dp[k][i] == math.inf:
      continue
    for j in range(N):
      dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

scores = [0] * N

for i in range(N):
  for j in range(N):
    if dp[i][j] != math.inf:
      scores[i] = max(scores[i], dp[i][j])

min_val = min(scores)

cnt = 0
cands = []
for i, score in enumerate(scores):
  if score == min_val:
    cnt += 1
    cands.append(i + 1)

print(f"{min_val} {cnt}")
print(" ".join(str(s) for s in cands))