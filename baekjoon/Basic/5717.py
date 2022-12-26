'''
==============================================================================================
@ Title: 상근이의 친구들
@ URL: https://www.acmicpc.net/problem/5717
@ Author: jopemachine
@ Created Date: 12/25/2022, 11:37:53 PM
@ Tags: arithmetic math
@ Level: Bronze 4
@ Description:
상근이의 남자 친구의 수와 여자 친구의 수가 주어졌을 때, 친구는 총 몇 명인지 구하는 프로그램을 작성하시오.
@ Input: 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 두 정수 M과 F로 이루어져 있으며, 각각은 상근이의 남자 친구의
수와 여자 친구의 수이다. (1 ≤ M, F ≤ 5) 입력의 마지막 줄에는 0이 두 개 주어진다.
@ Output: 각 테스트 케이스마다 상근이의 친구의 수를 출력한다.
==============================================================================================
'''

while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    print(a + b)