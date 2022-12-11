'''
==============================================================================================
@ Title: 대소문자 바꾸기
@ URL: https://www.acmicpc.net/problem/2744
@ Author: jopemachine
@ Created Date: 12/10/2022, 7:40:20 PM
@ Tags: implementation string
@ Level: Bronze 5
@ Description:
영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다. 단어의 길이는 최대 100이다.
@ Output: 첫째 줄에 입력으로 주어진 단어에서 대문자는 소문자로, 소문자는 대문자로 바꾼 단어를 출력한다.
==============================================================================================
'''

str_ = input()
ans = ''
for ch in str_:
    if ch.islower():
        ans += ch.upper()
    else:
        ans += ch.lower()
print(ans)