'''
==============================================================================================
@ Title: 별 찍기 - 3
@ URL: https://www.acmicpc.net/problem/2440
@ Author: jopemachine
@ Created Date: 12/17/2022, 10:03:11 PM
@ Tags: implementation
@ Level: Bronze 4
@ Description:
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
@ Input: 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
@ Output: 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
==============================================================================================
'''

N = int(input())

for i in range(N):
    for j in range(N - i):
        print('*', end='')
    print()
