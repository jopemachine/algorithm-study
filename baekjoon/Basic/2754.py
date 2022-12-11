'''
==============================================================================================
@ Title: 학점계산
@ URL: https://www.acmicpc.net/problem/2754
@ Author: jopemachine
@ Created Date: 12/10/2022, 7:43:14 PM
@ Tags: implementation string
@ Level: Bronze 5
@ Description:
어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오. A+: 4.3, A0: 4.0, A-:
3.7 B+: 3.3, B0: 3.0, B-: 2.7 C+: 2.3, C0: 2.0, C-: 1.7 D+: 1.3, D0: 1.0,
D-: 0.7 F: 0.0
@ Input: 첫째 줄에 C언어 성적이 주어진다. 성적은 문제에서 설명한 13가지 중 하나이다.
@ Output: 첫째 줄에 C언어 평점을 출력한다.
==============================================================================================
'''

grades = {
  'A+': 4.3,
  'A0': 4.0,
  'A-': 3.7,
  'B+': 3.3,
  'B0': 3.0,
  'B-': 2.7,
  'C+': 2.3,
  'C0': 2.0,
  'C-': 1.7,
  'D+': 1.3,
  'D0': 1.0,
  'D-': 0.7,
  'F': 0.0,
}

print(grades[input()])
