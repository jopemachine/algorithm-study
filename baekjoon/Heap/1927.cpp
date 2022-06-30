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

#ifdef BOJ
constexpr bool LOCAL = false;
#else
constexpr bool LOCAL = true;
#endif

#define ll long long

class PriorityQueue {
public:
  vector<int> heap;

  PriorityQueue() {}

  void push(int num) {
    heap.push_back(num);
    int current = heap.size() - 1;
    int parent = (current - 1) / 2;

    while (parent >= 0 && heap[current] < heap[parent]) {
      swap(heap[current], heap[parent]);
      current = parent;
      parent = (current - 1) / 2;
    }
  }

  int pop() {
    int ret = heap[0];
    heap[0] = heap.back();
    heap.pop_back();

    int current = 0;
    int left = 1, right = 2;

    while (left < heap.size()) {
      bool run = false;

      if (heap[current] > heap[left]) {
        swap(heap[current], heap[left]);
        current = left;
        run = true;
      }
      if (right < heap.size() && heap[current] > heap[right]) {
        swap(heap[current], heap[right]);
        current = right;
        run = true;
      }

      if (!run) break;

      left = 2 * current + 1;
      right = 2 * current + 2;
    }

    return ret;
  }
};

int solve () {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  auto pq = PriorityQueue();
  int N;
  cin >> N;

  for (int i = 0; i < N; ++i) {
    int opr;
    cin >> opr;

    if (opr == 0 && pq.heap.size() == 0) {
      cout << 0 << "\n";
    } else if (opr == 0) {
      cout << pq.pop() << "\n";
    } else {
      pq.push(opr);
    }
  }
  return 0;
}