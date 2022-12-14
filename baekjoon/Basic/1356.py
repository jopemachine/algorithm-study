'''
==============================================================================================
@ Title: 유진수
@ URL: https://www.acmicpc.net/problem/1356
@ Author: jopemachine
@ Created Date: 12/14/2022, 9:37:46 PM
@ Tags: arithmetic implementation math string
@ Level: Bronze 1
@ Description:
유진수는 어떤 수를 10진수로 표현한 뒤 그 수를 두 부분으로 나눴을 때, 앞부분 자리수의 곱과 뒷부분 자리수의 곱이 같을 때를
말한다. 예를 들어, 1221은 유진수이다. 12와 21로 나눴을 때, 앞부분 자리수의 곱 1*2는 뒷부분 자리수의 곱 2*1과 같기
때문이다. 1236도 마찬가지로 유진수이다. 하지만, 1234는 아니다. 수를 나눌 때 항상 연속된 자리수를 나눠야하고, 각 부분에
적어도 한자리는 있어야 한다. 예를 들어, 12345는 총 4가지 방법으로 나눌 수 있다. 1-2345, 12-345, 123-45,
1234-5 어떤 수 N이 주어질 때, 이 수가 유진수인지 아닌지 구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 수 N이 주어진다. 이 수는 2,147,483,647보다 작거나 같은 자연수이다.
@ Output: 첫째 줄에 N이 유진수이면 YES, 아니면 NO를 출력한다.
==============================================================================================
'''
import math

N = input()

ans = False
if len(N) != 1:
    for i in range(len(N)):
        left = math.prod(map(int, list(N[:i])))
        right = math.prod(map(int, list(N[i:])))

        if left == right:
            ans = True

print("YES" if ans else "NO")
