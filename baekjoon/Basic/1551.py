'''
==============================================================================================
@ Title: 수열의 변화
@ URL: https://www.acmicpc.net/problem/1551
@ Author: jopemachine
@ Created Date: 12/18/2022, 5:11:07 PM
@ Tags: implementation math parsing simulation string
@ Level: Bronze 1
@ Description:
크기가 N인 수열 A가 주어졌을 때, 세준이는 인접한 두 원소의 차이를 이용해서 크기가 N-1인 수열 B를 만들 수 있다. 예를 들어,
A = {5, 6, 3, 9, -1} 이었을 때, B = {6-5, 3-6, 9-3, -1-9} = {1, -3, 6, -10}이
된다. 즉, B[i] = A[i+1]-A[i]가 된다. 수열 A가 주어졌을 때, 세준이가 위의 방법을 K번 했을 때 나오는 수열을
구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 수열의 크기 N과 K가 주어진다. N은 20보다 작거나 같은 자연수이고, K는 0보다 크거나 같고, N-1보다 작거나 같은
정수이다. 둘째 줄에는 수열이 ‘,’로 구분되어 주어진다. 수열을 이루고 있는 수는 절댓값이 100보다 작거나 같은 정수이다.
@ Output: 첫째 줄에 K번 변형한 수열을 ‘,’로 구분하여 출력한다.
==============================================================================================
'''

N, K = map(int, input().split())
arr = list(map(int, input().split(',')))

res = arr

for i in range(K):
    new_res = []
    for j in range(len(res) - 1):
        new_res.append(res[j + 1] - res[j])
    res = new_res

print(",".join(map(str, res)))
