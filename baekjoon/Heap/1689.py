'''
==============================================================================================
@ Title: 겹치는 선분
@ URL: https://www.acmicpc.net/problem/1689
@ Author: jopemachine
@ Created Date: 9/25/2022, 4:52:29 PM
@ Description:
1차원 좌표계 위에 선분 N개가 있다. 선분이 최대로 겹쳐있는 부분의 겹친 선분의 개수를 구해보자. 선분의 끝 점에서 겹치는 것은
겹치는 것으로 세지 않는다.
@ Input: 첫째 줄에는 선분의 개수(1 ≤ N ≤ 1,000,000)가 입력으로 들어온다. 그 다음 N개의 줄에 선분의 시작 좌표 s와 끝나는
좌표 e (s < e)가 입력으로 들어온다. 선분의 좌표는 절댓값이 10억보다 작거나 같은 정수이다.
@ Output: 첫째 줄에는 최대로 많이 겹치는 선분들의 개수를 출력한다.
@ Ref: https://velog.io/@dbtlwns/%EB%B0%B1%EC%A4%80-%EA%B2%B9%EC%B9%98%EB%8A%94-%EC%84%A0%EB%B6%84-1689
==============================================================================================
'''
import heapq

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

min_heap = []
min_heap.append(lines[0][1])

ans = 1
for i in range(1, len(lines)):
  left, right = lines[i]
  while len(min_heap) != 0 and min_heap[0] <= lines[i][0]:
    heapq.heappop(min_heap)

  heapq.heappush(min_heap, right)
  ans = max(ans, len(min_heap))

print(ans)