'''
==============================================================================================
@ Title: 거짓말
@ URL: https://www.acmicpc.net/problem/1043
@ Author: jopemachine
@ Created Date: 10/10/2022, 3:33:18 PM
@ Description:
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다. 지민이는 그
이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다. 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에,
되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을
안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다. 당연히, 어떤 사람이 어떤 파티에서는
진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야
한다. 사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다.
지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을
구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다. 둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는
사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다. 셋째 줄부터 M개의
줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다. N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0
이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.
@ Output: 첫째 줄에 문제의 정답을 출력한다.
==============================================================================================
'''

N, M = map(int, input().split())

_, *know_true = list(map(int, input().split()))

parties = list(list(map(int, input().split())) for _ in range(M))

union_find = [0, *(i + 1 for i in range(N))]

def find(i):
  if union_find[i] == i:
    return i

  return find(union_find[i])

def union(i, j):
  i = find(i)
  j = find(j)

  # 이미 같은 루트
  if i == j:
    return

  # i를 루트로 결합
  if i in know_true:
    union_find[j] = i
  # j를 루트로 결합
  elif j in know_true:
    union_find[i] = j
  # 아무나 루트로 (i로) 결합
  else:
    union_find[j] = i

for _, *party in parties:
  u = party[0]
  for i in range(1, len(party)):
    union(u, party[i])

res = 0

for _, *party in parties:
  ok = True
  for u in party:
    if find(u) in know_true:
      ok = False
      break

  if ok:
    res += 1

print(res)
