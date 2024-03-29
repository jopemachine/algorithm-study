'''
==============================================================================================
@ Title: 계단 수
@ URL: https://www.acmicpc.net/problem/1562
@ Author: jopemachine
@ Created Date: 4/30/2023, 4:03:37 PM
@ Tags: bitmask dp dp_bitfield
@ Level: Gold 1
@ Description:
45656이란 수를 보자. 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다. N이 주어질 때, 길이가 N이면서
0부터 9까지 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 0으로 시작하는 수는 계단수가 아니다.
@ Input: 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
@ Output: 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
@ Ref: 백준 알고리즘 강의
==============================================================================================
'''

N = int(input())

# 점화식을 세우기 위해 필요한 변수는 수의 길이, 마지막 수, 사용한 숫자들.
# 각각을, i, j, k라고 하면,
# D[i][j][k]를 D[i + 1][j + 1][k - (1 << (j + 1))]와 D[i + 1][j - 1][k - (1 << (j - 1))]에 더해주면 된다.

D = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10):
    D[1][i][1 << i] = 1

for i in range(1, N):
    for j in range(0, 10):
        for k in range(0, 1 << 10):
            if (k & (1 << j)) == 0:
                continue

            if j + 1 <= 9:
                D[i + 1][j + 1][k | (1 << (j + 1))] += D[i][j][k]
                D[i + 1][j + 1][k | (1 << (j + 1))] %= 1000000000
            if j - 1 >= 0:
                D[i + 1][j - 1][k | (1 << (j - 1))] += D[i][j][k]
                D[i + 1][j - 1][k | (1 << (j - 1))] %= 1000000000

ans = 0
for i in range(0, 10):
    ans += D[N][i][(1 << 10) - 1]
    ans %= 1000000000

print(ans)
