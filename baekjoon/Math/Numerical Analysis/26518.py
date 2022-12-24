'''
==============================================================================================
@ Title: 수열의 극한값
@ URL: https://www.acmicpc.net/problem/26518
@ Author: jopemachine
@ Created Date: 12/25/2022, 12:42:41 AM
@ Tags: bruteforcing math
@ Level: Silver 3
==============================================================================================
'''

b, c, a1, a2 = map(int, input().split())

prev_value = a2 / a1
idx = 3

pprev_a = a1
prev_a = a2

ans = None
while True:
    curr_a = b * prev_a + c * pprev_a
    curr_value = curr_a / prev_a

    if abs(curr_value - prev_value) < (10 ** -6):
        ans = curr_value
        break

    pprev_a = prev_a
    prev_a = curr_a
    prev_value = curr_value

print(ans)