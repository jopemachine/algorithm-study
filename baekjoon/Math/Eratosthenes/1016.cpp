/*
==============================+===============================================================
@ Title : 제곱 ㄴㄴ 수
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

bool isSquareNoNoNumber[1000001];
int main() {
  _FASTIOS;
  ll min, max;
  cin >> min >> max;

  for (ll i = 2; i * i <= max; ++i) {
    for (ll j = start; j <= max - min; j += i * i) {
      isSquareNoNoNumber[j] = true;
    }
  }

  int ans = 0;

  for (int i = 0; i <= max - min; i++) {
    if (isSquareNoNoNumber[i] == 0) {
      ans++;
    }
  }
  cout << ans << '\n';
  return 0;
}