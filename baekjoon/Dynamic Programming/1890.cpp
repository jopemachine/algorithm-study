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
#define endl '\n'

#ifdef BOJ
constexpr bool LOCAL = false;
#else
constexpr bool LOCAL = true;
#endif

int main() {
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  int N;
  cin >> N;
  vector<vector<int>> map(N, vector<int>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> map[i][j];
    }
  }

  vector<vector<int>> dp(N, vector<int>(N, 0));
  dp[0][0] = 1;

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      if (map[i][j] == 0) continue;
      if (map[i][j] + i < N) {
        dp[map[i][j] + i][j] += dp[i][j];
      }
      if (map[i][j] + j < N) {
        dp[i][map[i][j] + j] += dp[i][j];
      }
    }
  }

  // for (int i = 0; i < N; ++i) {
  //   for (int j = 0; j < N; ++j) {
  //     cout << dp[i][j] << " ";
  //   }
  //   cout << "\n";
  // }
  cout << dp[N - 1][N - 1] << "\n";

  return 0;
}