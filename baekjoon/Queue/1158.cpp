/*
==============================================================================================
@ Title: 요세푸스 문제
@ URL: https://www.acmicpc.net/problem/1158
@ Created Date: 2022. 7. 8. 오전 10:40:51
@ Description:
요세푸스 문제는 다음과 같다. 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제
순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의
사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7,
3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다. N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을
작성하시오.
@ Input: 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
@ Output: 예제와 같이 요세푸스 순열을 출력한다.
==============================================================================================
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
  int N, K;
  cin >> N >> K;

  queue<int> que;
  for (int i = 0; i < N; ++i) {
    que.push(i + 1);
  }

  int top;
  int cntBuf = 0;
  vector<int> result;
  while (!que.empty()) {
    tie (top) = que.front();
    que.pop();

    if (++cntBuf == K) {
      result.push_back(top);
      cntBuf = 0;
    } else {
      que.push(top);
    }
  }

  cout << "<";
  for (int i = 0; i < N; ++i) {
    cout << result[i];
    if (i != N - 1) cout << ", ";
  }
  cout << ">";

  return 0;
}
