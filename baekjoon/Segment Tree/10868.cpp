/*
==============================+===============================================================
@ Title : 최솟값
@ Desc :
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

void init(vector<int>& tree, vector<int>& nums, int node, int s, int e) {
  if (s == e) {
    tree[node] = nums[s];
  } else {
    // 왼쪽 자식은 2*node, 오른쪽 자식은 2*node + 1에 있으니 각각을
    // init으로 초기화 하고, 최솟값을 뽑아오자.
    init(tree, nums, node * 2, s, (s + e) / 2);
    init(tree, nums, node * 2 + 1, (s + e) / 2 + 1, e);
    tree[node] = min(tree[node * 2], tree[node * 2 + 1]);
  }
}

int query(vector<int>& tree, int node, int s, int e, int i, int j) {
  // 세그먼트와 교집합이 없음
  if (i > e || j < s) {
    return -1;
  }
  // 찾으려는 구간이 세그먼트보다 더 작은 구간인 경우 => 최솟값을 해당 구간의 최솟값으로 특정 가능
  if (i <= s && e <= j) {
    return tree[node];
  }

  int left = query(tree, 2 * node, s, (s + e) / 2, i, j);
  int right = query(tree, 2 * node + 1, (s + e) / 2 + 1, e, i, j);

  if (left == -1) {
    return right;
  }
  if (right == -1) {
    return left;
  }

  return min(left, right);
}
int main() {
  _FASTIOS;
  int N, M;
  cin >> N >> M;
  vector<int> nums(N);
  vector<int> tree(4 * N);

  for (int i = 0; i < N; ++i) {
    cin >> nums[i];
  }

  init(tree, nums, 1, 0, N - 1);

  for (int i = 0; i < M; ++i) {
    int a, b;
    cin >> a >> b;
    cout << query(tree, 1, 0, N - 1, a - 1, b - 1) << '\n';
  }

  return 0;
}