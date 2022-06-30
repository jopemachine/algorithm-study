/*
==============================+===============================================================
@ Title : 카드 구매하기 3
@ Desc : 스택으로 푸는 게 정해 같은데, 유니온 파인드로 풀 수도 있는 문제였다.
스택으로 푸는 것도 어려운데 유니온 파인드 응용으로 풀 수 있는 걸 알아차리는 것도 쉽지 않았고,
유니온 파인드로 풀 수 있는 걸 알았어 구현도 쉽지 않았다..

값의 순서를 매겨 순회하되, 연속된 구간인지 파악하기 위해 인덱스 정보를 같이 저장하고,
부모는 자기 자신으로, 사이즈 정보를 1로 놓은 후 왼쪽과 병합, 오른쪽과 병합.
@ Ref : 백준 알고리즘 중급
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

int parents[1000001];
int ranks[1000001];
int sizes[1000001];

int find(int u) {
  // 일반적인 유니온파인드와 다른 부분.
  // -1로 초기화 해, 이 숫자가 방문된 숫자인지 알 수 있도록 만든다.
  if (u == -1) return -1;
  if (u == parents[u]) return u;
  return parents[u] = find(parents[u]);
}

// 일반적인 유니온 파인드와 다르게 사이즈를 계산해서 리턴해주도록 변형.
ll merge(int u, int v) {
  u = find(u);
  v = find(v);
  if (u == v || u == -1 || v == -1) return 0;
  // u의 랭크가 더 크도록 스왑
  if (ranks[u] < ranks[v]) swap(u, v);
  // 랭크가 더 큰 쪽이 위로, 더 작은 쪽이 밑으로 가게 해 트리 높이가 증가하지 않는다.
  parents[v] = u;

  // 랭크가 같은 경우 예외: 부모가 된 u의 랭크가 1 증가.
  if (ranks[u] == ranks[v]) {
    ranks[u] = ranks[v] + 1;
  }

  ll cnt = 1LL * sizes[u] * sizes[v];
  sizes[u] += sizes[v];
  return cnt;
}

void init() {
  memset(parents, -1, sizeof parents);
  memset(sizes, 0, sizeof sizes);
  memset(ranks, 0, sizeof ranks);
}
int main() {
  _FASTIOS;
  int N;
  cin >> N;
  vector<pii> pairs(N);

  // 연속된 구간 -> 인덱스와 함께 저장.
  for (int i = 0; i < N; ++i) {
    cin >> pairs[i].first;
    pairs[i].second = i;
  }

  sort(pairs.begin(), pairs.end());
  ll ans = 0;
  init();

  int num, idx;
  // 해당 값을 최댓값으로 포함하는 구간의 최댓값을 모두 구한다.
  for (int i = 0; i < N; ++i) {
    tie(num, idx) = pairs[i];
    parents[idx] = idx;
    sizes[idx] = 1;

    // 오른쪽과 병합
    if (idx + 1 < N) {
      ans += 1LL * num * merge(idx, idx + 1);
    }

    // 왼쪽과 병합
    if (idx - 1 >= 0) {
      ans += 1LL * num * merge(idx, idx - 1);
    }
  }

  init();

  // 해당 값을 최솟값으로 포함하는 구간의 최솟값을 모두 구한다.
  // 어차피 pairs는 변하지 않았으니 다시 정렬할 필요 없이 뒤 부터 보면 됨.
  for (int i = N - 1; i >= 0; --i) {
    tie(num, idx) = pairs[i];
    parents[idx] = idx;
    sizes[idx] = 1;

    if (idx + 1 < N) {
      ans -= 1LL * num * merge(idx, idx + 1);
    }
    if (idx - 1 >= 0) {
      ans -= 1LL * num * merge(idx, idx - 1);
    }
  }

  cout << ans << "\n";

  return 0;
}