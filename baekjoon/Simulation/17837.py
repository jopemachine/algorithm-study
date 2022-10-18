'''
==============================================================================================
@ Title: 새로운 게임 2
@ URL: https://www.acmicpc.net/problem/17837
@ Author: jopemachine
@ Created Date: 10/14/2022, 3:18:21 PM
@ Description:
재현이는 주변을 살펴보던 중 체스판과 말을 이용해서 새로운 게임을 만들기로 했다. 새로운 게임은 크기가 N×N인 체스판에서 진행되고,
사용하는 말의 개수는 K개이다. 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다. 체스판의 각 칸은 흰색, 빨간색, 파란색
중 하나로 색칠되어있다. 게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리
정해져 있다. 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다. 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는
것이다. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다. 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와
같다. 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다. A번 말이 이동하려는 칸이 흰색인 경우에는 그 칸으로
이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다. A번 말의 위에 다른 말이 있는 경우에는 A번
말과 위에 있는 모든 말이 이동한다. 예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한
후에는 D, E, A, B, C가 된다. 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로
바꾼다. A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다. A, D, F, G가 이동하고,
이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다. 파란색인 경우에는 A번 말의 이동
방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다. 체스판을
벗어나는 경우에는 파란색과 같은 경우이다. 다음은 크기가 4×4인 체스판 위에 말이 4개 있는 경우이다. 첫 번째 턴은 다음과 같이
진행된다. 두 번째 턴은 다음과 같이 진행된다. 체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때, 게임이 종료되는 턴의
번호를 구해보자.
@ Input: 첫째 줄에 체스판의 크기 N, 말의 개수 K가 주어진다. 둘째 줄부터 N개의 줄에 체스판의 정보가 주어진다. 체스판의 정보는 정수로
이루어져 있고, 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다. 다음 K개의 줄에 말의 정보가 1번 말부터
순서대로 주어진다. 말의 정보는 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향이다. 행과 열의 번호는 1부터
시작하고, 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다. 같은 칸에 말이 두 개 이상
있는 경우는 입력으로 주어지지 않는다.
@ Output: 게임이 종료되는 턴의 번호를 출력한다. 그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력한다.
==============================================================================================
'''

N, K = map(int, input().split())

_map = list(list(map(int, input().split())) for _ in range(N))

dr = [0,0,-1,1]
dc = [1,-1,0,0]

players = list(list(map(int, input().split())) for _ in range(K))
players = list(map(lambda x: [x[0] - 1, x[1] - 1, x[2] - 1], players))

players_map = [[[] for _ in range(N)] for _ in range(N)]

for idx, (r, c, k) in enumerate(players):
  players_map[r][c].append(idx)

turn_counter = 0
flag = False

def is_game_ended():
  for r in range(N):
    for c in range(N):
      if len(players_map[r][c]) >= 4:
        return True
  return False

def reverse_dir(d):
  if d in [0, 2]:
    d += 1
  elif d in [1, 3]:
    d -= 1
  else:
    assert False
  return d

def move_player(player_idx, r, c, nr, nc, should_reverse):
  arr_idx = players_map[r][c].index(player_idx)

  moved = players_map[r][c][arr_idx:] if not should_reverse else list(reversed(players_map[r][c][arr_idx:]))
  players_map[nr][nc] += moved
  players_map[r][c] = players_map[r][c][:arr_idx]

  for moved_player_idx in moved:
    players[moved_player_idx][0], players[moved_player_idx][1] = nr, nc

while turn_counter <= 1000:
  turn_counter += 1

  # 1번 플레이어 부터 순서대로 움직인다.
  for player_idx, (r, c, k) in enumerate(players):
    nr = r + dr[k]
    nc = c + dc[k]

    # 범위가 안 맞거나 이동하려는 방향이 파란색인 경우
    if not (0 <= nr < N and 0 <= nc < N) or _map[nr][nc] == 2:
      # 방향을 반대로 한다.
      r_k = reverse_dir(k)

      nnr = r + dr[r_k]
      nnc = c + dc[r_k]

      # 방향을 반대로 한 후 이동한 방향이 파란색이거나 범위에서 벗어날 경우, 해당 말의 방향만 바꾸고 움직이지 않는다
      if not (0 <= nnr < N and 0 <= nnc < N) or _map[nnr][nnc] == 2:
        players[player_idx][2] = r_k
      else:
        players[player_idx] = [nnr, nnc, r_k]
        move_player(player_idx, r, c, nnr, nnc, _map[nnr][nnc] == 1)

    # 범위가 맞고, 이동하려는 칸이 파란색이 아닌 경우
    else:
      players[player_idx] = [nr, nc, k]
      move_player(player_idx, r, c, nr, nc, _map[nr][nc] == 1)

    if is_game_ended():
      flag = True
      break

  if flag:
    break

print(turn_counter if turn_counter <= 1000 else -1)