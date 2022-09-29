'''
==============================================================================================
@ Title: 수 고르기
@ URL: https://www.acmicpc.net/problem/2230
@ Author: jopemachine
@ Created Date: 9/29/2022, 1:14:03 PM
@ Description:
N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그
차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오. 예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 만약 M
= 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 이 중에서 차이가 가장 작은 경우는 1 4나 2 5를
골랐을 때의 3이 된다.
@ Input: 첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.
@ Output: 첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 항상 차이가 M이상인 두 수를 고를 수 있다.
==============================================================================================
'''
import math

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

nums.sort()

i = 0
j = 0
min_diff = math.inf

while i <= j and i < N and j < N:
  # print(f"i: {i}, j: {j}")
  if nums[j] - nums[i] >= M:
    min_diff = min(min_diff, nums[j] - nums[i])
    i += 1
  else:
    j += 1

print(min_diff)