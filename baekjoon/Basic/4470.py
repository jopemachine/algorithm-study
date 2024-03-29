'''
==============================================================================================
@ Title: 줄번호
@ URL: https://www.acmicpc.net/problem/4470
@ Author: jopemachine
@ Created Date: 12/25/2022, 11:24:21 PM
@ Tags: implementation string
@ Level: Bronze 4
@ Description:
텍스트에서 줄을 입력받은 뒤, 줄 번호를 출력하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 줄의 수 N이 주어진다. 둘째 줄부터 N개의 줄에 각 줄의 내용이 주어진다. 각 줄에 있는 글자의 개수는 50글자를 넘지
않는다.
@ Output: 각 문장의 앞에 줄 번호를 추가한 뒤 출력한다. 줄 번호는 1번부터 시작한다. 줄번호를 추가하는 형식은 출력 예제를 참고하면 된다.
==============================================================================================
'''

N = int(input())
for i in range(1, N + 1):
    print(f"{i}. {input()}")
