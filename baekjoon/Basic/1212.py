'''
==============================================================================================
@ Title: 8진수 2진수
@ URL: https://www.acmicpc.net/problem/1212
@ Author: jopemachine
@ Created Date: 1/6/2023, 7:30:22 PM
@ Tags: implementation math string
@ Level: Bronze 2
@ Description:
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 8진수가 주어진다. 주어지는 수의 길이는 333,334을 넘지 않는다.
@ Output: 첫째 줄에 주어진 수를 2진수로 변환하여 출력한다. 수가 0인 경우를 제외하고는 반드시 1로 시작해야 한다.
==============================================================================================
'''
N = int(input(), 8)
print(bin(N)[2:])

