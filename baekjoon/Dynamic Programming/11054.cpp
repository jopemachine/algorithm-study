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

#define ll long long;

int N;

int nums[1001];
// 길이, 비교 순서가 꺽이는 점이 나왔는지 여부
int dp[1001][2];

int main() {
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  cin >> N;

  for (int i = 0; i < N; ++i) {
    cin >> nums[i];
  }

  int maxVal = 0;

  for (int i = 0; i < N; ++i) {
    memset(dp, -1, sizeof(dp));
    maxVal = max(maxVal, go(i, 0));
  }

  cout << maxVal << "\n";

  return 0;
}