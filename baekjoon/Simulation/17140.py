'''
==============================================================================================
@ Title: 이차원 배열과 연산
@ URL: https://www.acmicpc.net/problem/17140
@ Author: jopemachine
@ Created Date: 9/26/2022, 7:17:59 PM
@ Description:
크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다. R 연산: 배열 A의
모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다. C 연산: 배열 A의 모든 열에 대해서 정렬을
수행한다. 행의 개수 < 열의 개수인 경우에 적용된다. 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야
한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 그 다음에는 배열 A에 정렬된
결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다. 예를 들어, [3,
1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 다시 이 배열에는 3이 1번,
1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다. 정렬된 결과를 배열에 다시 넣으면 행 또는
열의 크기가 달라질 수 있다. R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C 연산이 적용된 경우에는
가장 큰 열을 기준으로 모든 열의 크기가 변한다. 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야
한다. 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다. 행 또는 열의 크기가 100을 넘어가는
경우에는 처음 100개를 제외한 나머지는 버린다. 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이
k가 되기 위한 최소 시간을 구해보자.
@ Input: 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100) 둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다.
배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.
@ Output: A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 100초가 지나도 A[r][c] = k가 되지 않으면
-1을 출력한다.
@ Ref: https://www.acmicpc.net/problem/17140
@ Note:
문제 자체는 그냥 빡구현 문제이다.
구현하다보면 R, C 연산을 따로 구현하는 식으로 풀 필요가 없다는 걸 알게 된다.
C 연산을 이미 구현한 R 연산으로 구현하면 되는데 이 과정에서 배열을 연산 전 한 번, 연산 후 한 번 뒤집어줘야 한다.
그리고 길이가 100 넘어가지 않도록 중간 과정의 리스트 길이가 50을 넘을 때 잘라줘야 하고, 
튜플들의 리스트를 2차원 배열로 만드는 과정을 직접하면 시간 초과가 나기 때문에 reduce 함수를 쓰는 등 효율적으로 구현해줘야 한다.
그 외 배열을 뒤집을 때 zip을 사용해 뒤집을 수 있다는 것과, 파이썬에선 Counter란 게 있어서 직접 딕셔너리로 배열내의 숫자들을 세 줄 필요가 없단 걸 알게 되었다.
==============================================================================================
'''

from collections import Counter
from functools import reduce

R, C, K = map(int, input().split())

R -= 1
C -= 1

array = [list(map(int, input().split())) for _ in range(3)]

elapsed_time = 0

while (len(array) <= R or len(array[0]) <= C) or array[R][C] != K:
  if elapsed_time >= 100:
    elapsed_time = -1
    break

  should_flip = False
  row_cnt = len(array)
  col_cnt = len(array[0])

  if row_cnt < col_cnt:
    array = list(map(list, zip(*array)))
    should_flip = True
    row_cnt, col_cnt = col_cnt, row_cnt

  # 각각의 행들을 돌면서 각 숫자의 출현 갯수를 세서 counter에 딕셔너리로 저장.
  # 딕셔너리를 튜플 형태로 바꿔 출현 갯수, 숫자의 오름차순으로 정렬한 후
  # 1차원 배열로 변환해 원래 배열을 대체.
  for i in range(row_cnt):
    counter = Counter(array[i])
    del counter[0]

    counter_list = list(counter.items())
    counter_list.sort(key=lambda x: (x[1], x[0]))

    if len(counter_list) > 50:
      counter_list = counter_list[:50]

    array[i] = reduce(lambda x, y: list(x) + list(y), counter_list[1:], list(counter_list[0]))

  # 최대 길이의 row를 찾고, 나머지 row들을 해당 row의 길이에 맞춰준다.
  # (array에 접근할 때 KeyError를 피하기 위함)
  max_col_len = 0
  for i in range(row_cnt):
    max_col_len = max(max_col_len, len(array[i]))

  for i in range(row_cnt):
    if len(array[i]) < max_col_len:
      array[i].extend([0] * (max_col_len - len(array[i])))

  if should_flip:
    array = list(map(list, zip(*array)))
    row_cnt, col_cnt = col_cnt, row_cnt

  elapsed_time += 1

if len(array) > R and len(array[0]) > C and array[R][C] != K:
  print(-1)
else:
  print(elapsed_time)