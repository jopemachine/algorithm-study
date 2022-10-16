'''
==============================================================================================
@ Title: ACM Craft
@ URL: https://www.acmicpc.net/problem/1005
@ Author: jopemachine
@ Created Date: 10/13/2022, 2:57:52 PM
@ Description:
서기 2012년! 드디어 2년간 수많은 국민들을 기다리게 한 게임 ACM Craft (Association of Construction
Manager Craft)가 발매되었다. 이 게임은 지금까지 나온 게임들과는 다르게 ACM크래프트는 다이나믹한 게임 진행을 위해 건물을
짓는 순서가 정해져 있지 않다. 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다. 매 게임시작 시 건물을 짓는
순서가 주어진다. 또한 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.   위의 예시를 보자. 이번
게임에서는 다음과 같이 건설 순서 규칙이 주어졌다. 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. (동시에 진행이
가능하다) 그리고 4번 건물을 짓기 위해서는 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다. 따라서
4번건물의 건설을 완료하기 위해서는 우선 처음 1번 건물을 건설하는데 10초가 소요된다. 그리고 2번 건물과 3번 건물을 동시에
건설하기 시작하면 2번은 1초뒤에 건설이 완료되지만 아직 3번 건물이 완료되지 않았으므로 4번 건물을 건설할 수 없다. 3번 건물이
완성되고 나면 그때 4번 건물을 지을수 있으므로 4번 건물이 완성되기까지는 총 120초가 소요된다. 프로게이머 최백준은 애인과의 데이트
비용을 마련하기 위해 서강대학교배 ACM크래프트 대회에 참가했다! 최백준은 화려한 컨트롤 실력을 가지고 있기 때문에 모든 경기에서 특정
건물만 짓는다면 무조건 게임에서 이길 수 있다. 그러나 매 게임마다 특정건물을 짓기 위한 순서가 달라지므로 최백준은 좌절하고
있었다. 백준이를 위해 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.
@ Input: 첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 첫째 줄에 건물의 개수 N과 건물간의
건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다)  둘째 줄에는 각 건물당 건설에 걸리는 시간
D1, D2, ..., DN이 공백을 사이로 주어진다. 셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은
다음에 건물 Y를 짓는 것이 가능하다는 의미이다)  마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.
@ Output: 건물 W를 건설완료 하는데 드는 최소 시간을 출력한다. 편의상 건물을 짓는 명령을 내리는 데는 시간이 소요되지 않는다고 가정한다.
건설순서는 모든 건물이 건설 가능하도록 주어진다.
==============================================================================================
'''
from math import inf
from heapq import heappush, heappop

T = int(input())

for _ in range(T):
  N, K = map(int, input().split())
  Ds = list(map(int, input().split()))

  _map = [[False] * N for _ in range(N)]
  indegrees = [0] * N

  for s, e in [list(map(int, input().split())) for _ in range(K)]:
    _map[s - 1][e - 1] = True
    indegrees[e - 1] += 1

  W = int(input())

  min_heap = []

  for i in range(N):
    if indegrees[i] == 0:
      heappush(min_heap, (Ds[i], i))

  min_cost = inf

  while min_heap:
    total_cost, curr = heappop(min_heap)

    if curr == W - 1:
      min_cost = total_cost
      break

    for next in range(N):
      if _map[curr][next]:
        indegrees[next] -= 1

        if indegrees[next] <= 0:
          heappush(min_heap, (total_cost + Ds[next], next))

  print(min_cost)