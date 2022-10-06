'''
==============================================================================================
@ Title: 좋은수열
@ URL: https://www.acmicpc.net/problem/2661
@ Author: jopemachine
@ Created Date: 10/5/2022, 2:54:28 PM
@ Description:
숫자 1, 2, 3으로만 이루어지는 수열이 있다. 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜
수열이라고 부른다. 그렇지 않은 수열은 좋은 수열이다. 다음은 나쁜 수열의 예이다. 33 32121323 123123213 다음은 좋은
수열의 예이다. 2 32 32123 1232123 길이가 N인 좋은 수열들을 N자리의 정수로 보아 그중 가장 작은 수를 나타내는 수열을
구하는 프로그램을 작성하라. 예를 들면, 1213121과 2123212는 모두 좋은 수열이지만 그 중에서 작은 수를 나타내는 수열은
1213121이다.
@ Input: 입력은 숫자 N하나로 이루어진다. N은 1 이상 80 이하이다.
@ Output: 첫 번째 줄에 1, 2, 3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력한다. 수열을
이루는 1, 2, 3들 사이에는 빈칸을 두지 않는다.
@ Ref: https://lu-coding.tistory.com/74
==============================================================================================
'''

N = int(input())

finished = False

def is_bad_seq(str):
  if not str:
    return False

  for i in range(1, (len(str) // 2) + 1):
    right = str[-i:]
    left = str[-2*i: -i]

    if left == right:
      return True

  return False

def solve(str):
  global finished

  if finished or is_bad_seq(str):
    return

  if len(str) >= N:
    finished = True
    print(str)
    return

  solve(str + "1")
  solve(str + "2")
  solve(str + "3")

solve("")
