'''
==============================================================================================
@ Title: 부호
@ URL: https://www.acmicpc.net/problem/1247
@ Author: jopemachine
@ Created Date: 12/26/2022, 10:57:08 PM
@ Tags: arbitrary_precision arithmetic math
@ Level: Bronze 3
@ Description:
N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.
@ Input: 총 3개의 테스트 셋이 주어진다. 각 테스트 셋의 첫째 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄부터 N개의 줄에
걸쳐 각 정수가 주어진다. 주어지는 정수의 절댓값은 9223372036854775807보다 작거나 같다.
@ Output: 총 3개의 줄에 걸쳐 각 테스트 셋에 대해 N개의 정수들의 합 S의 부호를 출력한다. S=0이면 "0"을, S>0이면 "+"를,
S<0이면 "-"를 출력하면 된다.
==============================================================================================
'''
T = 3
for _ in range(T):
    N = int(input())
    sum = 0
    for _ in range(N):
        sum += int(input())
    if sum == 0:
        print("0")
    elif sum > 0:
        print("+")
    else:
        print("-")
