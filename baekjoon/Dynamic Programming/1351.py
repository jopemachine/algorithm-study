'''
==============================================================================================
@ Title: 무한 수열
@ URL: https://www.acmicpc.net/problem/1351
@ Author: jopemachine
@ Created Date: 10/9/2022, 11:35:22 AM
@ Description:
무한 수열 A는 다음과 같다. A0 = 1 Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1) N, P와 Q가 주어질 때, AN을
구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 3개의 정수 N, P, Q가 주어진다.
@ Output: 첫째 줄에 AN을 출력한다.
==============================================================================================
'''

N, P, Q = map(int, input().split())

dp = {}
dp[0] = 1

# 바텀업 방식 => 딕셔너리 사용하더라도 메모리 초과
# idx = 1
# while idx <= N:
#   dp[idx] = dp[idx // P] + dp[idx // Q]
#   idx += 1

def topdown(idx):
  if idx < 1:
    return 1

  if idx in dp:
    return dp[idx]

  dp[idx] = topdown(idx // P) + topdown(idx // Q)
  return dp[idx]

print(topdown(N))
