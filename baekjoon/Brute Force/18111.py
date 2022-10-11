'''
==============================================================================================
@ Title: 마인크래프트
@ URL: https://www.acmicpc.net/problem/18111
@ Author: jopemachine
@ Created Date: 10/11/2022, 1:02:06 PM
@ Description:
팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다. 마인크래프트는 1 × 1 × 1(세로, 가로,
높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다. 목재를 충분히 모은 lvalue는
집을 짓기로 하였다. 하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야
한다. lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터
내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다. 좌표 (i, j)의 가장 위에 있는
블록을 제거하여 인벤토리에 넣는다. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. 1번 작업은
2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다. ‘땅
고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오. 단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터
바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수
없으며, 음수가 될 수 없다.
@ Input: 첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107) 둘째 줄부터 N개의 줄에 각각
M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의
높이는 256보다 작거나 같은 자연수 또는 0이다.
@ Output: 첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을
출력하시오.
==============================================================================================
'''
from itertools import chain
from math import inf

N, M, B = map(int, input().split())

# 굳이 이차원 배열로 생각할 필요가 없다.
# 합치고 내림차순으로 정렬하자
arr = sorted(chain.from_iterable(list(list(map(int, input().split())) for _ in range(N))), reverse=True)

# 블록 높이의 범위가 0~256까지 밖에 되지 않는다는 점을 이용해서
# 타겟 높이를 미리 정해두고 모든 땅 높이를 거기까지 맞출 때 까지 걸리는 
# 시간들의 최솟값을 정해보자.
min_time = inf
res_height = -1

# 높이 k로 모두 동일하게 맞추는 경우.
for k in range(257):
  time = 0
  ok = True
  holding_block_cnt = B

  for i in range(N * M):
    # 맞추려는 높이가 더 큰 경우 
    if arr[i] < k:
      # 이 이상의 높이로는 맞출 수 없음
      if holding_block_cnt < k - arr[i]:
        ok = False
        break
      # 블록을 인벤토리에서 꺼낸 갯수만큼 시간을 소요하고, 인벤토리에서 꺼냄.
      time += (k - arr[i])
      holding_block_cnt -= (k - arr[i])

    # 블록의 높이가 맞추려는 높이보다 큰 경우
    elif arr[i] > k:
      # 블록을 깨서 인벤토리에 넣음.
      time += (arr[i] - k) * 2
      holding_block_cnt += arr[i] - k

  if not ok:
    break

  if min_time >= time:
    min_time = time
    res_height = k

print(f"{min_time} {res_height}")

