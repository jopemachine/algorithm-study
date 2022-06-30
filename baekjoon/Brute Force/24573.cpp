/*
==============================+===============================================================
@ Title : Good Fours and Good Fives
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

int dp[1000001];

int go (int n) {
  // cout << n << "\n";
  if (n < 4) return 0;
  if (n == 4 || n == 5) {
    return 1;
  }

  // int& ans = dp[n];
  // if (ans != -1) return ans;

  return go (n - 4) + go (n - 5);
}
int main() {
  _FASTIOS;
  int N;
  cin >> N;
  memset(dp, -1, sizeof dp);
  cout << go(N) << '\n';

  return 4;
}