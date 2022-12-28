'''
==============================================================================================
@ Title: Fill the Rowboats!
@ URL: https://www.acmicpc.net/problem/5300
@ Author: jopemachine
@ Created Date: 12/28/2022, 10:09:29 PM
@ Tags: implementation
@ Level: Bronze 4
@ Description:
Captain Jack decides to to take over a rival’s ship. He needs to send his
henchmen over on rowboats that can hold 6 pirates each. You will help him
count out pirates in groups of 6. The last rowboat may have fewer than 6
pirates. To make your task easier each pirate has been assigned a number
from 1 to N.
@ Input: The input will be N, the number of pirates you need to send over on
rowboats.
@ Output: The output will be the number of each pirate separated by spaces, with the
word ”Go!” after every 6th pirate, and after the last pirate.
==============================================================================================
'''

N = int(input())

for i in range(1, N + 1):
    print(i, end=' ')

    if i % 6 == 0:
        print('Go!', end=' ')

if N % 6 != 0:
    print('Go!', end=' ')
