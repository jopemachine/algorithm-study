/*
==============================+===============================================================
@ Title: 팔
@ URL: https://www.acmicpc.net/problem/1105
@ Date: 7/6/2022, 12:06:21 PM
@ Text:
L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를
구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 L과 R이 주어진다. L은 2,000,000,000보다 작거나 같은 자연수이고, R은 L보다 크거나 같고,
2,000,000,000보다 작거나 같은 자연수이다.
@ Output: 첫째 줄에 L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을
작성하시오.
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

  string L, R;
  cin >> L >> R;
  if (L.size() != R.size()) {
    cout << 0 << '\n';
    return 0;
  }

  int result = 0;
  for (int i = 0; i < L.size(); ++i) {
    if (L[i] != R[i]) break;
    if (L[i] == '8' && R[i] == '8') {
      ++result;
    }
  }

  cout << result;

  return 0;
}
