'''
==============================================================================================
@ Title: 가장 긴 감소하는 부분 수열
@ URL: https://www.acmicpc.net/problem/11722
@ Author: jopemachine
@ Created Date: 9/26/2022, 12:07:19 PM
@ Description:
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오. 예를 들어, 수열 A = {10, 30, 10,
20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는
3이다.
@ Input: 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤
Ai ≤ 1,000)
@ Output: 첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.
==============================================================================================
'''
N = int(input())
lis = list(map(int, input().split()))

dp = [-1] * 1000

def fn(idx):
  if dp[idx] != -1:
    return dp[idx]

  ret = 1
  dp[idx] = 1

  for i in range(idx + 1, len(lis)):
    if lis[i] < lis[idx]:
      ret = max(ret, fn(i) + 1)
      dp[idx] = ret

  return ret

res = 0
for i in range(N):
  res = max(res, fn(i))

print(res)