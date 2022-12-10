'''
==============================================================================================
@ Title: 엄청난 부자2
@ URL: https://www.acmicpc.net/problem/1271
@ Author: jopemachine
@ Created Date: 12/9/2022, 11:59:40 PM
@ Tags: arbitrary_precision arithmetic math
@ Level: Bronze 5
@ Description:
갑부 최백준 조교는 동전을 최소로 바꾸는데 성공했으나 김재홍 조교가 그 돈을 발견해서 최백준 조교에게 그 돈을 나누자고 따진다. 그
사실이 전 우주로 알려지자 우주에 있던 많은 생명체들이 자신들에게 돈을 분배해 달라고 당장 달려오기 시작했다. 프로토스 중앙 우주
정부의 정책인, ‘모든 지적 생명체는 동등하다’라는 규칙에 입각해서 돈을 똑같이 분배하고자 한다. 한 생명체에게 얼마씩 돈을 줄 수
있는가? 또, 생명체들에게 동일하게 분배한 후 남는 돈은 얼마인가?
@ Input: 첫째 줄에는 최백준 조교가 가진 돈 n과 돈을 받으러 온 생명체의 수 m이 주어진다. (1 ≤ m ≤ n ≤ 101000, m과 n은
10진수 정수)
@ Output: 첫째 줄에 생명체 하나에게 돌아가는 돈의 양을 출력한다. 그리고 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력한다.
==============================================================================================
'''

N, M = map(int, input().split())

x = N // M
print(x)
print(N % M)
