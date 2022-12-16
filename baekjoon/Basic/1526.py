'''
==============================================================================================
@ Title: 가장 큰 금민수
@ URL: https://www.acmicpc.net/problem/1526
@ Author: jopemachine
@ Created Date: 12/16/2022, 10:31:00 PM
@ Tags: bruteforcing implementation math
@ Level: Bronze 1
@ Description:
은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다. N이 주어졌을 때,
N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 N이 주어진다. N은 4보다 크거나 같고 1,000,000보다 작거나 같은 자연수이다.
@ Output: 첫째 줄에 N보다 작거나 같은 금민수 중 가장 큰 것을 출력한다.
==============================================================================================
'''

N = int(input())

ans = None
for i in range(N, 0, -1):
    if str(i).count('4') + str(i).count('7') == len(str(i)):
        ans = i
        break

print(i)
