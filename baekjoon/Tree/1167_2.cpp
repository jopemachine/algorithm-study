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

vector<pii> tree[100001];

int answers[100001];
bool visited[100001];

int longest;

int getMaxWeight(int node) {
  vector<pii>& childs = tree[node];

  int dest, weight;
  vector<int> possibleHeights;

  for (auto it = childs.begin(); it != childs.end(); ++it) {
    tie(dest, weight) = (*it);
    if (visited[dest]) continue;

    visited[dest] = true;
    int height = getMaxWeight(dest) + weight;
    possibleHeights.push_back(height);
  }

  if (possibleHeights.empty()) return 0;

  if (possibleHeights.size() >= 2) {
    sort(possibleHeights.begin(), possibleHeights.end());

    longest = max(
      longest,
        possibleHeights[possibleHeights.size() - 1] +
        possibleHeights[possibleHeights.size() - 2]
    );
  }

  return possibleHeights.back();
}
int main() {
  _FASTIOS;
  int N;
  cin >> N;

  for (int i = 1; i <= N; ++i) {
    int idx;
    cin >> idx;

    while (true) {
      int dest, weight;
      cin >> dest;
      if (dest == -1) break;
      cin >> weight;

      tree[idx].push_back({ dest, weight });
      tree[dest].push_back({ idx, weight });
    }
  }

  cout << max(longest, getMaxWeight(1)) << '\n';

  return 0;
}