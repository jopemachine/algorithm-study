/*
==============================+===============================================================
@ Title : 암호코드
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

string code;

int dp[5001][2];

int go (int k, int cnt) {
  int& ans = dp[k][cnt - 1];
  if (ans != -1) return ans;
  if (k > code.size()) return 1;

  ans = 0;
  for (int i = k + 1; i < code.size(); ++i) {
    if (stoi(code.substr(i - 1, 2)) <= 26) {
      ans += go (i, 1);
    }
    ans += go (i, 0);
  }

  return ans;
}
int main() {
  _FASTIOS;

  cin >> code;
  memset(dp, -1, sizeof dp);
  cout << go (0, 0);
  return 0;
}
