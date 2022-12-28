'''
==============================================================================================
@ Title: Gnome Sequencing
@ URL: https://www.acmicpc.net/problem/4589
@ Author: jopemachine
@ Created Date: 12/28/2022, 9:50:04 PM
@ Tags: implementation
@ Level: Bronze 4
@ Description:
In the book All Creatures of Mythology, gnomes are kind, bearded creatures,
while goblins tend to be bossy and simple-minded. The goblins like to
harass the gnomes by making them line up in groups of three, ordered by the
length of their beards. The gnomes, being of different physical heights,
vary their arrangements to confuse the goblins. Therefore, the goblins must
actually measure the beards in centimeters to see if everyone is lined up
in order. Your task is to write a program to assist the goblins in
determining whether or not the gnomes are lined up properly, either from
shortest to longest beard or from longest to shortest.
@ Input: The input starts with line containing a single integer N, 0 < N < 30, which
is the number of groups to process. Following this are N lines, each
containing three distinct positive integers less than 100.
@ Output: There is a title line, then one line per set of beard lengths. See the
sample output for capitalization and punctuation.
==============================================================================================
'''

N = int(input())
print("Gnomes:")
for i in range(N):
    nums = list(map(int, input().split()))
    if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
        print("Ordered")
    else:
        print("Unordered")