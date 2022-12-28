'''
==============================================================================================
@ Title: St. Ives
@ URL: https://www.acmicpc.net/problem/4696
@ Author: jopemachine
@ Created Date: 12/28/2022, 9:51:05 PM
@ Tags: arithmetic math
@ Level: Bronze 4
@ Description:
Robert the chapman (a medieval traveling merchant) made regular trips
between his home village and St. Ives to peddle his cloth, ribbons, and
needles. On one such trip he encountered a curious procession: As I was
traveling to St. Ives I met a man with seven wives. Every wife had seven
sacks. Every sack had seven cats. Every cat had seven kits. Kits, cats,
sacks, wives - How many were traveling to St. Ives? The answer to this
classic ancient riddle is ’one’. Robert was traveling to St. Ives. The
others were all traveling away from St. Ives. However, if we prefer to ask
the question of how many were traveling from St. Ives, we can add up: 1 man
7 wives 7*7 sacks 7*7*7 cats 7*7*7*7 kittens for a total of 2801. On his
next trip to St. Ives, Robert met the same man, this time accompanied by 3
wives, each with 3 sacks, and so on. Becoming curious about what seemed to
be a bizarre village ritual of some kind, Robert kept track of how many
traveled with the man each time he encountered him during the subsequent
year. On average, what was the size of the processions that Robert
encounter on his trips to St. Ives?
@ Input: Input consists of multiple data sets. Each data set consists of a line with
a single floating point number number representing the numbers of wives,
sacks per wife, cats per sack, and kittens per cat that Robert encountered
that year. End of input is indicated by a value of zero.
@ Output: For each data set, print the size of the average procession as a real
number presented to 2 decimal points precision.
==============================================================================================
'''
while True:
    N = float(input())
    if N == 0:
        break
    sum = 1 + (N) + (N * N) + (N * N * N) + (N * N * N * N)
    print(f"{sum:.2f}")
