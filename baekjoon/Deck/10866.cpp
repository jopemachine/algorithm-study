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

class Deque {
public:
  int begin;
  int end;
  vector<int> nums;

  Deque() {
    begin = 0;
    end = 0;
  }

  void push_back(int num) {
    nums.push_back(num);
    ++end;
  }

  void push_front(int num) {
    if (begin == 0 && end == 0) {
      nums.clear();
      nums.push_back(num);
      begin = end = 0;
      ++end;
    }
    // 동적 배열의 push_back 처럼 2배씩 앞으로 늘어나도록 구현하려함
    else if (begin <= 0) {
      // begin과 end가 같은 경우는 0, 0 밖에 없음.
      // push에선 end와 begin 간격이 멀어지고, 
      // pop_front, pop_back에선 begin과 end가 같아지면 초기화 하기 때문.
      assert(size() != 0);

      int newSize = 2 * size();

      vector<int> newNums(newSize);
      for (int i = begin; i < end; ++i) {
        newNums[i + size()] = nums[i];
      }
      begin = end - 1;
      newNums[begin] = num;
      end *= 2;

      nums = newNums;
    }
    else {
      --begin;
      nums[begin] = num;
    }
  }

  void pop_front() {
    if (begin == end) {
      return;
    }

    int ret = nums[begin];
    ++begin;

    if (begin == end) {
      begin = 0;
      end = 0;
      nums.clear();
    }
  }

  void pop_back() {
    if (begin == end) {
      return;
    }

    int ret = nums[end - 1];
    --end;

    if (begin == end) {
      begin = 0;
      end = 0;
      nums.clear();
    }
  }

  int front() {
    if (begin == end) return -1;
    return nums[begin];
  }

  int back() {
    if (begin == end) return -1;
    return nums[end - 1];
  }

  bool isEmpty() {
    return begin == end;
  }

  int size() {
    return end - begin;
  }
};
int main() {
  _FASTIOS;
  int N;
  cin >> N;
  Deque que;

  while (N--) {
    string str;
    cin >> str;
    if (str == "push_front") {
      int num;
      cin >> num;
      que.push_front(num);
    }
    else if (str == "push_back") {
      int num;
      cin >> num;
      que.push_back(num);
    }
    else if (str == "pop_front") {
      if (!que.size()) cout << -1 << "\n";
      else {
        cout << que.front() << "\n";
        que.pop_front();
      }
    }
    else if (str == "pop_back") {
      if (!que.size()) cout << -1 << "\n";
      else {
        cout << que.back() << "\n";
        que.pop_back();
      }
    }
    else if (str == "empty") {
      cout << (que.isEmpty() ? 1 : 0) << "\n";
    }
    else if (str == "front") {
      cout << que.front() << "\n";
    }
    else if (str == "back") {
      cout << que.back() << "\n";
    }
    else if (str == "size") {
      cout << que.size() << "\n";
    }
  }
  return 0;
}