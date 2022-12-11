'''
==============================================================================================
@ Title: 눈 치우기
@ URL: https://www.acmicpc.net/problem/26215
@ Author: jopemachine
@ Created Date: 12/11/2022, 10:37:47 PM
@ Tags: greedy implementation simulation sorting
@ Level: Silver 4
@ Description:
지난 밤 겨울 숲에는 눈이 많이 내렸다. 당신은 숲의 주민들을 위해 눈이 오지 않는 동안 모든 집 앞의 눈을 치우고자 한다. 당신은
1분에 한 번씩 두 집을 선택해서 두 집 앞의 눈을 각각 1만큼 치우거나, 한 집을 선택해서 그 집 앞의 눈을 1만큼 치울 수 있다.
모든 집 앞의 눈을 전부 치울 때까지 걸리는 최소 시간은 얼마일까?
@ Input: 첫 줄에 집의 수를 의미하는 정수 $N$ ($1 \leq N \leq 100$)이 주어진다. 다음 줄에는 각각의 집 앞에 쌓여 있는
눈의 양을 나타내는 정수 $a_{i}$ ($1 \leq a_{i} \leq 2000$)이 주어진다.
@ Output: 모든 집 앞의 눈을 치우는 데 최소 몇 분이 걸리는지를 출력한다. 24시간(1440분)이 넘게 걸릴 경우 -1을 출력한다.
==============================================================================================
'''

from heapq import heappush, heappop

N = int(input())
arr = map(int, input().split())
# N = 1
# arr = [1440]

max_heap = []
for i in arr:
    heappush(max_heap, -i)

t = 0
while t <= 1440:
    if not max_heap or max_heap[0] == 0:
        break

    r1 = -heappop(max_heap)

    if not max_heap or max_heap[0] == 0:
        heappush(max_heap, -(r1 - 1))
        t += 1
        continue

    r2 = -heappop(max_heap)

    heappush(max_heap, -(r1 - 1))
    heappush(max_heap, -(r2 - 1))
    t += 1


if t > 1440:
    t = -1

print(t)
