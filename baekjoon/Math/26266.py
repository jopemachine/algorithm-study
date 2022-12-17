'''
==============================================================================================
@ Title: 비즈네르 암호 해독
@ URL: https://www.acmicpc.net/problem/26266
@ Author: jopemachine
@ Created Date: 12/17/2022, 9:27:15 PM
@ Tags: 
@ Level: Unrated
@ Description:
비즈네르 암호는 고전 암호의 일종으로, 대문자 알파벳으로만 이뤄진 평문에 키를 더하여 암호를 만드는 방법이다. 구체적인 과정은 다음과
같다. 평문과 동일한 길이가 될 때까지 키를 반복하여 문자열을 만든다. 이 문제에선 키를 단순 반복해 평문과 동일한 길이를 만들 수
있는 경우만 고려한다. 평문과 키의 각 알파벳을 1부터 26까지의 수에 순서대로 대응시켜 수열을 만든다. 즉, A=1, B=2,
..., Z=26가 된다. 평문과 키 수열에서 동일한 위치에 있는 수들을 더하여 암호문을 만든다. 단, 더했을 때 26이 넘는 수의
경우 26만큼 뺀 결과를 사용한다. 2와 마찬가지로, 암호문에서 수를 다시 알파벳에 대응시켜 문자열로 만들고 최종 결과로 반환한다.
예를 들어, 평문이 HELLOWORLD이고, 키가 SCUPC라고 하자. 1에서 키를 두 번 반복해 SCUPCSCUPC가 되며, 2에서
수에 대응시키면 키는 $[19, 3, 21, 16, 3, 19, 3, 21, 16, 3]$, 평문인 HELLOWORLD는 $[8, 5,
12, 12, 15, 23, 15, 18, 12, 4]$가 된다. 이후 3에서 동일한 위치에 있는 수를 더하면 $[27, 8, 33,
28, 18, 42, 18, 39, 28, 7]$이며, 26 초과인 수에서 26을 빼면 $[1, 8, 7, 2, 18, 16, 18,
13, 2, 7]$이 된다. 이를 다시 알파벳에 대응시키면, 최종 결과는 AHGBRPRMBG가 된다. 평문과 임의의 키를 사용해 만든
비즈네르 암호문이 주어질 때, 가능한 키 중 가장 짧은 키를 찾아보자.
@ Input: 첫 번째 줄에 평문이 주어진다. 평문은 알파벳 대문자로만 구성되어 있으며, 평문의 길이는 $200\,000$을 넘지 않는다. 두 번째
줄에 평문에 대한 비즈네르 암호문이 주어진다. 암호문은 알파벳 대문자로만 구성되어 있으며, 주어진 평문과 동일한 길이를 가진다. 올바른
비즈네르 암호문이 주어지며, 답이 항상 존재함이 보장된다.
@ Output: 첫 번째 줄에 가능한 키 중 가장 짧은 키를 출력한다.
==============================================================================================
'''

str = input()
pw = input()

alphabets = {}
for i, ch in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alphabets[ch] = i + 1

str_nums = [alphabets[ch] for ch in str]
pw_nums = [alphabets[ch] for ch in pw]

num_to_alphabets = [*alphabets.keys()]

r_str = ""
for pw_num, str_num in zip(pw_nums, str_nums):
    diff = pw_num - str_num
    if diff < 0:
        diff += 26

    r_str += num_to_alphabets[(diff - 1) % 26]

ans = None
for i in range(len(str)):
    substr = r_str[i:]

    if len(str) % len(substr) == 0:
        if substr * (len(r_str) // len(substr)) == r_str:
            ans = substr

print(ans)
