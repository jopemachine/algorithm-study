'''
==============================================================================================
@ Title: 빈도 정렬
@ URL: https://www.acmicpc.net/problem/2910
@ Author: jopemachine
@ Created Date: 12/17/2022, 7:06:48 PM
@ Tags: data_structures hash_set sorting
@ Level: Silver 2
@ Description:
위대한 해커 창영이는 모든 암호를 깨는 방법을 발견했다. 그 방법은 빈도를 조사하는 것이다. 창영이는 말할 수 없는 방법을 이용해서
현우가 강산이에게 보내는 메시지를 획득했다. 이 메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 창영이는 이
숫자를 자주 등장하는 빈도순대로 정렬하려고 한다. 만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는
경우에는 X가 Y보다 앞에 있어야 한다. 만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다. 이렇게 정렬하는 방법을
빈도 정렬이라고 한다. 수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 메시지의 길이 N과 C가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ C ≤ 1,000,000,000) 둘째 줄에 메시지
수열이 주어진다.
@ Output: 첫째 줄에 입력으로 주어진 수열을 빈도 정렬한 다음 출력한다.
==============================================================================================
'''

N, C = map(int, input().split())
input_arr = map(int, input().split())

freq = {}

for i, num in enumerate(input_arr):
    if not freq.get(num):
        freq[num] = [1, i]
    else:
        freq[num][0] += 1

arr = []
for num, v in freq.items():
    count, first = v
    if count != 0:
        arr.append((num, count, first))

res = sorted(arr, key=lambda x: (-x[1], x[2]))

for item in res:
    print(f"{str(item[0])} " * item[1], end="")
