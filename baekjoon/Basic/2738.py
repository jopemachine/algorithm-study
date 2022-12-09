'''
==============================================================================================
@ Title: 행렬 덧셈
@ URL: https://www.acmicpc.net/problem/2738
@ Author: jopemachine
@ Created Date: 12/10/2022, 12:21:22 AM
@ Tags: implementation math
@ Level: Bronze 5
@ Description:
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에
행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
@ Output: 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
==============================================================================================
'''

N, M = map(int, input().split())
A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

C = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

for i in range(N):
    for j in range(M):
        print(C[i][j], end=' ')
    print()
