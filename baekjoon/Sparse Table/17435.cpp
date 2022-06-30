/*
==============================+===============================================================
@ Title : 합성함수와 쿼리
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

// log 200000 = 17 정도..
// 그래서 18 사용.
int sparseTable[200001][18];
int main() {
  _FASTIOS;
  int M;
  cin >> M;
  for (int i = 1; i <= M; ++i) {
    cin >> sparseTable[i][0];
  }

  // 2의 j 제곱 꼴로 희소 배열을 만든다.
  for (int j = 1; j <= 18; ++j) {
    for (int i = 1; i <= M; ++i) {
      sparseTable[i][j] = sparseTable[sparseTable[i][j - 1]][j - 1];
    }
  }

  int Q;
  cin >> Q;

  while (Q--) {
    int N, ans;
    cin >> N >> ans;
    // f^n(X)를 이진수의 원리로 각 자릿 수 마다 (2^k씩) 움직여서 lgN에 구하자!
    for (int i = 0; i <= 18; ++i) {
      if (N & (1 << i)) {
        ans = sparseTable[ans][i];
      }
    }

    cout << ans << '\n';
  }

  return 0;
}