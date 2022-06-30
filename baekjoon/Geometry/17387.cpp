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

using Point = pair<long long, long long>;
using Line = pair<Point, Point>;

int ccw(Point P1, Point P2, Point P3) {
  long long front = P1.first * P2.second + P2.first * P3.second + P3.first * P1.second;
  long long back = P1.second * P2.first + P2.second * P3.first + P3.second * P1.first;
  long long out = front - back;

  if (out == 0) return 0;
  else if (out > 0) {
    return 1;
  }
  else {
    return -1;
  }
}

bool cross(Line L1, Line L2) {
  int l1l2 = ccw(L1.first, L1.second, L2.first) * ccw(L1.first, L1.second, L2.second);
  int l2l1 = ccw(L2.first, L2.second, L1.first) * ccw(L2.first, L2.second, L1.second);

  if (l1l2 == 0 && l2l1 == 0) {
    if (L1.first > L1.second) {
      swap(L1.first, L1.second);
    }
    if (L2.first > L2.second) {
      swap(L2.first, L2.second);
    }

    // pair를 이용한 비교에 유의.
    // L1의 큰 점이 L2의 작은 점 보다 크고, L1의 작은 점이 L2의 큰 점 보다 작다면,
    // 세 점이 한 일직선 위에 있으면서 교차한다
    return L1.second >= L2.first && L1.first <= L2.second;
  }

  return l2l1 <= 0 && l1l2 <= 0;
}

int main() {
  cin.tie(NULL);
  ios::sync_with_stdio(false);
  Point P1, P2, P3, P4;
  cin >> P1.first >> P1.second;
  cin >> P2.first >> P2.second;
  cin >> P3.first >> P3.second;
  cin >> P4.first >> P4.second;

  Line L1 = {P1, P2};
  Line L2 = {P3, P4};

  cout << (cross(L1, L2) ? 1 : 0) << "\n";
  return 0;
}