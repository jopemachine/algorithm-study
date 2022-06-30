/*
==============================+===============================================================
@ Title : 최소비용 구하기 2
@ Desc : 역추적 알고리즘은 값이 변할 때 왜 바뀌었는지를 기록할 것.
그렇게 하면 재귀나 스택으로 실제 값을 재구성할 수 있음.
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

struct Edge {
  int to;
  int cost;
  Edge(int to, int cost): to(to), cost(cost) {};
};

const int INF = 1e9;

vector<Edge> graph[1001];
int dist[1001];
int froms[1001];
bool visited[1001];

void reconstruct (vector<int>& paths, int start) {
  if (dist[start] != 0) {
    reconstruct(paths, froms[start]);
  }
  paths.push_back(start);
}
int main() {
  _FASTIOS;
  int V, E;
  cin >> V >> E;

  for (int i = 0; i < E; ++i) {
    int from, to, cost;
    cin >> from >> to >> cost;
    graph[from].push_back(Edge(to, cost));
  }

  for (int i = 1; i <= V; ++i) {
    dist[i] = INF;
    froms[i] = INF;
  }

  int start, end;
  cin >> start >> end;

  dist[start] = 0;

  priority_queue<pii> pQue;

  pQue.push({0, start});

  int cost, dest;

  while (!pQue.empty()) {
    tie(cost, dest) = pQue.top();
    pQue.pop();

    if (visited[dest]) continue;
    visited[dest] = true;

    vector<Edge>& linkedList = graph[dest];

    for (Edge edge : linkedList) {
      if (dist[edge.to] > dist[dest] + edge.cost) {
        dist[edge.to] = dist[dest] + edge.cost;
        froms[edge.to] = dest;
        pQue.push({ -dist[edge.to], edge.to });
      }
    }
  }

  cout << dist[end] << "\n";

  vector<int> paths;
  reconstruct(paths, end);
  cout << paths.size() << '\n';
  for (int i = 0; i < paths.size(); ++i) {
    cout << paths[i] << ' ';
  }

  return 0;
}