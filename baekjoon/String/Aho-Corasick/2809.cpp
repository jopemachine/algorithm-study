// 백준 알고리즘 중급
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

struct Node {
  map<int, int> childs;
  // 불일치 했을 때 다음 노드가 무엇인지 나타내는, fail 함수
  int pi;
  int len;
  Node () {
    len = 0;
    pi = -1;
  }
};

vector<Node> trie;

int init() {
  Node root;
  trie.push_back(root);
  return (int) trie.size() - 1;
}

void add(int root, string str, int idx) {
  if (idx >= str.length()) {
    trie[root].len = idx;
    return;
  }

  int childIdx = str[idx] - 'a';
  if (trie[root].childs.count(childIdx) == 0) {
    int next = init();
    trie[root].childs[childIdx] = next;
  }

  add(trie[root].childs[childIdx], str, idx + 1);
}

int getNext(int trieRoot, int node, char ch) {
  int childIdx = ch - 'a';
  while (trieRoot != node && trie[node].childs.count(childIdx) == 0) {
    node = trie[node].pi;
  }
  if (trie[node].childs.count(childIdx) > 0) {
    node = trie[node].childs[childIdx];
  }
  return node;
}
int main() {
  _FASTIOS;

  int N, M;
  cin >> N;
  string street;
  cin >> street;
  cin >> M;
  int trieRoot = init();

  // 아호코라식 적용을 위한 트라이 만듬
  for (int i = 0; i < M; ++i) {
    string str;
    cin >> str;
    add(trieRoot, str, 0);
  }

  queue<int> que;
  trie[trieRoot].pi = trieRoot;
  que.push(trieRoot);

  // BFS로 pi 갱신
  while (!que.empty()) {
    int node = que.front();
    que.pop();
    for (int i = 0; i < 26; ++i) {
      if (trie[node].childs.count(i) == 0) continue;
      int next = trie[node].childs[i];

      if (node == trieRoot) {
        trie[next].pi = trieRoot;
      }

      else {
        int x = trie[node].pi;
        while (x != trieRoot && trie[x].childs.count(i) == 0) {
          x = trie[x].pi;
        }
        if (trie[x].childs.count(i) > 0) {
          x = trie[x].childs[i];
        }
        trie[next].pi = x;
      }
      int pi = trie[next].pi;
      // 여기서 len을 추가로 더해주는 부분이 일반적인 아호코라식과 다른 유일한 부분..
      trie[next].len = max(trie[next].len, trie[pi].len);
      que.push(next);
    }
  }

  // 스위핑 하기 위해 각각의 시작 인덱스, 끝 인덱스를 넣어줌.
  vector<pii> matches;
  int node = trieRoot;

  // 매 문자마다 트라이를 돌면서 검색해주면 된다. 
  for (int i = 0; i < street.size(); ++i) {
    node = getNext(trieRoot, node, street[i]);
    // len이 0 보다 크다면 포함하는 경우이므로 문자열이 시작할 때의 인덱스와
    // 끝날 때의 인덱스를 넣어줌, second 값은 -1이면 시작, 1이면 끝.
    if (trie[node].len > 0) {
      matches.push_back({ i - trie[node].len + 1, -1 });
      matches.push_back({ i, 1 });
    }
  }

  // 스위핑 하면서 몇 개인지 셈.
  int ans = 0;
  sort(matches.begin(), matches.end());
  int start = 0;
  int open = 0;

  // 겹치는 선분 문제는 여러 방식으로 풀 수 있는데...
  // 일관된 방식을 하나 정해서 그걸로만 푸는 게 좋을 것 같다.
  for (auto& match : matches) {
    if (match.second == -1) {
      if (open == 0) start = match.first;
      open += 1;
    } else {
      open -= 1;
      if (open == 0) ans += match.first - start + 1;
    }
  }

  cout << street.length() - ans << "\n";

  return 0;
}