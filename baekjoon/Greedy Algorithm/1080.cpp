/*
==============================+===============================================================
@ Title: 행렬
@ URL: https://www.acmicpc.net/problem/1080
@ Date: 7/4/2022, 1:59:37 PM
@ Text:
0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을
작성하시오. 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
@ Input: 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고,
그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
@ Output: 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.
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

  int N, M;
  cin >> N >> M;

  vector<vector<int>> metricA(N, vector<int>(M));
  for (int i = 0; i < N; ++i) {
    string tmp;
    cin >> tmp;
    for (int j = 0; j < M; ++j) {
      metricA[i][j] = (tmp[j] - '0');
    }
  }

  vector<vector<int>> metricB(N, vector<int>(M));
  for (int i = 0; i < N; ++i) {
    string tmp;
    cin >> tmp;
    for (int j = 0; j < M; ++j) {
      metricB[i][j] = (tmp[j] - '0');
    }
  }

  int result = 0;

  for (int i = 0; i < N - 2; ++i) {
    for (int j = 0; j < M - 2; ++j) {
      if (metricA[i][j] != metricB[i][j]) {
        ++result;
        for (int di = 0; di < 3; ++di) {
          for (int dj = 0; dj < 3; ++dj) {
            metricA[i + di][j + dj] = 1 - metricA[i + di][j + dj];
          }
        }
      }
    }
  }

  bool isSame = true;

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      if (metricA[i][j] != metricB[i][j]) {
        isSame = false;
        break;
      }
    }
  }

  cout << (isSame ? result : -1);
  return 0;
}

