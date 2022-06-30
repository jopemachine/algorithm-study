/*
==============================+===============================================================
@ Title : 제곱 ㄴㄴ
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

vector<int> squares;

bool isSquareNoNo[100001];

// 포함-배제 원리로 M의 제곱 ㄴㄴ수가 몇 개 인지 구한다.
int go(int idx, ll num, ll M) {
  if (idx >= squares.size()) return 0;
  if (num * squares[idx] > M) return 0;

  int ans = 0;
  ans += (M / (num * squares[idx]));
  ans += go(idx + 1, num, M);
  ans -= go(idx + 1, num * squares[idx], M);

  return ans;
}
int main() {
  _FASTIOS;
  int K;
  cin >> K;

  // 제곱 수들을 모두 미리 구해놓자.
  for (ll i = 2; i <= 100000; ++i) {
    if (isSquareNoNo[i]) continue;
    squares.push_back(i * i);

    for (ll j = i * i; j <= 100000; j += i) {
      isSquareNoNo[j] = true;
    }
  }

  ll left = 0;
  ll right = 2147483647;
  ll ans = right;

  // 이분 탐색하며 mid 값이 몇 개의 제곱 ㄴㄴ수를 갖는지
  // 포함 배제 원리로 구한다.
  while (left <= right) {
    ll mid = (left + right) / 2;
    // cnt는 mid에서 제곱 ㄴㄴ수 갯수를 뺀 것이니, 앞에 몇 개의 제곱 ㄴㄴ 수가 있는지 나타냄.
    int cnt = mid - go (0, 1, mid);

    if (cnt >= K) {
      ans = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  cout << ans << '\n';

  return 0;
}