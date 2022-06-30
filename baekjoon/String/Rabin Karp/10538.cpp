/*
==============================+===============================================================
@ Title : 빅 픽쳐
@ Desc : 라빈카프 알고리즘 이용한 풀이
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

ll mod = 2147483647;
// o를 1로, x를 0으로 보면 두 개 밖에 없으므로 2를 쓴다. (경험과 운..)
int base = 2;

vector<int> convert(string & str) {
  vector<int> ret(str.length(), 0);

  for (int i = 0; i < ret.size(); ++i) {
    if (str[i] == 'o') {
      str[i] = 1;
    }
  }
  return ret;
}
int main() {
  _FASTIOS;
  int rs, cs, rb, cb;
  cin >> rs >> cs >> rb >> cb;

  vector<vector<int>> smallPic(rs);
  vector<vector<int>> bigPic(rb);

  for (int i = 0; i < rs; ++i) {
    string buf;
    cin >> buf;
    smallPic[i] = convert(buf);
  }

  for (int i = 0; i < rb; ++i) {
    string buf;
    cin >> buf;
    bigPic[i] = convert(buf);
  }


  return 0;
}