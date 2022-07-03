/*
==============================+===============================================================
@ Title: 토너먼트
@ URL: https://www.acmicpc.net/problem/1057
@ Date: 7/3/2022, 9:39:17 AM
@ Text:
김지민은 N명이 참가하는 스타 토너먼트에 진출했다. 토너먼트는 다음과 같이 진행된다. 일단 N명의 참가자는 번호가 1번부터 N번까지
배정받는다. 그러고 난 후에 서로 인접한 번호끼리 스타를 한다. 이긴 사람은 다음 라운드에 진출하고, 진 사람은 그 라운드에서
떨어진다. 만약 그 라운드의 참가자가 홀수명이라면, 마지막 번호를 가진 참가자는 다음 라운드로 자동 진출한다. 다음 라운드에선 다시
참가자의 번호를 1번부터 매긴다. 이때, 번호를 매기는 순서는 처음 번호의 순서를 유지하면서 1번부터 매긴다. 이 말은 1번과 2번이
스타를 해서 1번이 진출하고, 3번과 4번이 스타를 해서 4번이 진출했다면, 4번은 다음 라운드에서 번호 2번을 배정받는다. 번호를
다시 배정받은 후에 한 명만 남을 때까지 라운드를 계속 한다. 마침 이 스타 대회에 임한수도 참가했다. 김지민은 갑자기 스타 대회에서
우승하는 욕심은 없어지고, 몇 라운드에서 임한수와 대결하는지 궁금해졌다. 일단 김지민과 임한수는 서로 대결하기 전까지 항상 이긴다고
가정한다. 1 라운드에서 김지민의 번호와 임한수의 번호가 주어질 때, 과연 김지민과 임한수가 몇 라운드에서 대결하는지 출력하는
프로그램을 작성하시오.
@ Input: 첫째 줄에 참가자의 수 N과 1 라운드에서 김지민의 번호와 임한수의 번호가 순서대로 주어진다. N은 2보다 크거나 같고,
100,000보다 작거나 같은 자연수이고, 김지민의 번호와 임한수의 번호는 N보다 작거나 같은 자연수이고, 서로 다르다.
@ Output: 첫째 줄에 김지민과 임한수가 대결하는 라운드 번호를 출력한다. 만약 서로 대결하지 않을 때는 -1을 출력한다.
@ Desc :
@ Ref :
==============================+===============================================================
*/

#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <utility>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <tuple>
#include <algorithm>
#include <array>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define debug if constexpr (LOCAL) cout
#define _FASTIOS cin.tie(nullptr),cout.tie(nullptr),ios::sync_with_stdio(0)
#define endl '\n'
#define ll long long
#define pii pair<int, int>

#ifdef BOJ
constexpr bool LOCAL = false;
#else
constexpr bool LOCAL = true;
#endif

int tree[100001][17];

int main() {
  _FASTIOS;

  int N, A, B;
  cin >> N >> A >> B;

  // 다른 사람들 번호는 몰라도 관계 없음.
  tree[A][0] = A;
  tree[B][0] = B;

  if (N % 2 == 1) ++N;
  N /= 2;

  int r = 1;
  bool shouldEnd = false;
  while (N > 1) {
    for (int i = 1; i <= N; ++i) {
      int prevIdx = i * 2 - 1;

      if (
        (tree[prevIdx][r - 1] == A && tree[prevIdx + 1][r - 1] == B) ||
        (tree[prevIdx][r - 1] == B && tree[prevIdx + 1][r - 1] == A)
      ) {
        shouldEnd = true;
        break;
      }

      if (tree[prevIdx][r - 1] == A || tree[prevIdx + 1][r - 1] == A) {
        tree[i][r] = A;
      }
      if (tree[prevIdx][r - 1] == B || tree[prevIdx + 1][r - 1] == B) {
        tree[i][r] = B;
      }
    }

    if (shouldEnd) break;
    ++r;
    if (N % 2 == 1) ++N;
    N /= 2;
  }

  // 서로 반드시 이기기 때문에 항상 대결한다.
  // -1인 경우는 없음.
  cout << r;
  return 0;
}
