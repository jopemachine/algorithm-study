'''
==============================================================================================
@ Title: 논리학 교수
@ URL: https://www.acmicpc.net/problem/1813
@ Author: jopemachine
@ Created Date: 12/20/2022, 8:28:21 PM
@ Tags: ad_hoc bruteforcing
@ Level: Bronze 1
@ Description:
논리학 교수 양항승은 칠판에 다음과 같은 내용을 썼다. 정확하게 a개의 말은 참이다. 정확하게 b개의 말은 참이다. 정확하게 c개의
말은 참이다. ... ... ... a, b, c는 정수이다. 그리고 나서 항승이는 칠판에 작성한 내용 중에 총 몇 개가 참인지
알아내는 사람은 A+을 받는다. 입력으로 항승이가 작성한 내용에 있는 정수가 주어진다. 예를 들면, "정확하게 i개의 말은 참이다"
에서 i가 입력으로 주어진다.  항승이가 칠판에 작성한 내용이 주어졌을 때, 총 몇 개의 내용이 참인지 구해보자.
@ Input: 첫째 줄에 항승이가 한 말의 개수 N이 주어진다. N은 1보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄에 항승이가
칠판에 작성한 내용에 있는 정수가 주어진다. 이 정수는 50보다 작거나 같은 음이 아닌 정수이다.
@ Output: 첫째 줄에 항승이가 칠판에 작성한 내용 중 몇 개가 참인지 출력한다. 만약 내용이 모순이라면 -1을 출력하고, 가능한 답이
여러가지라면 가장 큰 값을 출력한다.
==============================================================================================
'''

N = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(1, 51):
    if i == arr.count(i):
        ans = i

if ans != 0:
    print(ans)
else:
    if 0 in arr:
        print(-1)
    else:
        print(0)
