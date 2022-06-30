#include <iostream>

using namespace std;

// boolean 배열을 추가해 O(1)에 중복 검사 가능
bool check[50 * 20 + 1];
int main() {
  int n;
  cin >> n;
  // 네 수의 합이 n이 된다는 점을 이용해 N^4을 N^3으로 만들 수 있음. 
  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= n - i; ++j) {
      for (int k = 0; k <= n - i - j; ++k) {
        int l = n - i - j - k;
        int sum = i + 5 * j + 10 + k + 50 * l;
        check[sum] = true;
      }
    }
  }

  int ans = 0;
  for (int i = 0; i <= 50 * 20; ++i) {
    if (check[i]) ans += 1;
  }
  cout << ans << "\n";
  return 0;
}