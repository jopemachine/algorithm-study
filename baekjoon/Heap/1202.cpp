/*
==============================================================================================
@ Title: 보석 도둑
@ URL: https://www.acmicpc.net/problem/1202
@ Created Date: 9/23/2022, 8:19:08 PM
@ Description:
세계적인 도둑 상덕이는 보석점을 털기로 결심했다. 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를
가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을
수 있다. 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
@ Input: 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000) 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다.
(0 ≤ Mi, Vi ≤ 1,000,000) 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤
100,000,000) 모든 숫자는 양의 정수이다.
@ Output: 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
==============================================================================================
*/
#include <iostream>
#include <vector>
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

using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
  if (a.first == b.first) {
      return a.second > b.second;
  }
  else {
      return a.first < b.first;
  }
}

int main() {
  int N, K;
  cin >> N >> K;

  vector<pair<int, int>> jewels(N);

  int M, V;
  for (int i = 0; i < N; ++i) {
    cin >> M >> V;
    jewels[i] = { M, V };
  }

  sort(jewels.begin(), jewels.end(), cmp);

  vector<int> bags(K);
  for (int i = 0; i < K; ++i) {
    cin >> bags[i];
  }

  sort(bags.begin(), bags.end());

  int idx = 0;
  long long sum = 0;

  priority_queue<int> pq;
  for (int i = 0; i < K; ++i) {
    while (idx < N && jewels[idx].first <= bags[i]) {
      pq.push(jewels[idx].second);
      ++idx;
    }

    if (!pq.empty()) {
      sum += pq.top();
      pq.pop();
    }
  }

  cout << sum << "\n";
  return 0;
}