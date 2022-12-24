'''
==============================================================================================
@ Title: 연속인가? ?
@ URL: https://www.acmicpc.net/problem/26517
@ Author: jopemachine
@ Created Date: 12/25/2022, 12:44:55 AM
@ Tags: calculus math
==============================================================================================
'''

import math
import sys

ellipsis = sys.float_info.epsilon

K = int(input())
a, b, c, d = map(int, input().split())

l = a * (K - ellipsis) + b
r = c * (K + ellipsis) + d

if math.isclose(l, r):
    print(f"Yes {a * K + b}")
else:
    print("No")
