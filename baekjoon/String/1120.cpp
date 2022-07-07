/*
==============================+===============================================================
@ Title: 문자열
@ URL: https://www.acmicpc.net/problem/1120
@ Date: 7/7/2022, 3:07:04 PM
@ Text:
길이가 N으로 같은 문자열 X와 Y가 있을 때, 두 문자열 X와 Y의 차이는 X[i] ≠ Y[i]인 i의 개수이다. 예를 들어,
X=”jimin”, Y=”minji”이면, 둘의 차이는 4이다. 두 문자열 A와 B가 주어진다. 이때, A의 길이는 B의 길이보다
작거나 같다. 이제 A의 길이가 B의 길이와 같아질 때 까지 다음과 같은 연산을 할 수 있다. A의 앞에 아무 알파벳이나 추가한다.
A의 뒤에 아무 알파벳이나 추가한다. 이때, A와 B의 길이가 같으면서, A와 B의 차이를 최소로 하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 A와 B가 주어진다. A와 B의 길이는 최대 50이고, A의 길이는 B의 길이보다 작거나 같고, 알파벳 소문자로만 이루어져
있다.
@ Output: A와 B의 길이가 같으면서, A와 B의 차이를 최소가 되도록 했을 때, 그 차이를 출력하시오.
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

#define debug          \
  if constexpr (LOCAL) \
  cout
#define _FASTIOS cin.tie(nullptr), cout.tie(nullptr), ios::sync_with_stdio(0)
#define endl '\n'
#define ll long long
#define pii pair<int, int>

#ifdef BOJ
constexpr bool LOCAL = false;
#else
constexpr bool LOCAL = true;
#endif

int main()
{
  _FASTIOS;

  string A, B;
  cin >> A >> B;

  int minDiff = 2e9;

  // 슬라이드할 A의 시작 위치
  for (int i = 0; i <= B.size() - A.size(); ++i) {
    // 이 경우의 최소 갯수를 세 주자.
    int diffCnt = 0;
    for (int j = 0; j < A.size(); ++j) {
      if (A[j] != B[i + j]) {
        ++diffCnt;
      }
    }

    minDiff = min(minDiff, diffCnt);
  }

  // 가장 최소가 되는 경우의 수
  cout << minDiff;

  return 0;
}