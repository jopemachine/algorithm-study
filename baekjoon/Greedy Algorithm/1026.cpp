/*
==============================+===============================================================
@ Title : 보물
@ Text:
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다. 길이가
N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자. S = A[0] × B[0] + ... + A[N-1] ×
B[N-1] S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다. S의 최솟값을 출력하는
프로그램을 작성하시오.
@ Input: 첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. N은
50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.
@ Output: 첫째 줄에 S의 최솟값을 출력한다.
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

  int N;
  cin >> N;
  vector<int> A(N);
  vector<int> B(N);
  for (int i = 0; i < N; ++i) {
    cin >> A[i];
  }
  for (int i = 0; i < N; ++i) {
    cin >> B[i];
  }

  sort(A.begin(), A.end());
  sort(B.begin(), B.end(), greater<int>());

  int res = 0;
  for (int i = 0; i < N; ++i) {
    res += A[i] * B[i];
  }

  cout << res << '\n';
  return 0;
}
