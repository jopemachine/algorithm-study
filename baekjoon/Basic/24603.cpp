/*
==============================+===============================================================
@ Title : Scaling Recipe
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
int main() {
  _FASTIOS;
  int N, X, Y;
  cin >> N >> X >> Y;

  for (int i = 0; i < N; ++i) {
    int tmp;
    cin >> tmp;
    cout << (tmp * Y) / X << '\n';
  }

  return 0;
}