/*
==============================+===============================================================
@ File Name : 11726.h
@ Author : jopemachine
@ Desc : 
@    2 * n 타일링
@    이런 종류의 DP 문제는 끙끙 앓으며 머리로 생각하는 것 보다 그림으로 몇 번 그려보면
@    점화식이 쉽게 보여 풀 수 있었다.
@    
@    왜 이렇게 풀리는 지 궁금해서 찾아보니,
@    왼쪽부터 오른쪽으로 채워나간다고 한다면, 2 x n개의 타일을 채우는 방법은
@     2 x (n - 1)개까지 채운 것의 오른쪽에 2 x 1 타일을 붙이는 경우와,  2 x (n - 2)개
@    까지 채운 것의 오른쪽에 1 x 2 타일을 2개 붙이는 경우로 나눌 수 있기 때문이라고 한다.
@    
@    그 외 10007이란 10000보다 큰 최소의 소수로 중간 답을 나눠 오버 플로우가 나지 않게 해야
@    한다는 것도 알아두자
@    (결과 값을 10007로 %한 것과 중간 결과마다 10007로 %한 결과가 같다!)
==============================+===============================================================
*/
#ifndef ALGORITHM_11726_H
#define ALGORITHM_11726_H

#include <iostream>
#include <string>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
   int N;
   cin >> N;

   int f[N + 1];
   f[0] = 0;
   f[1] = 1;
   f[2] = 2;

   for(int i = 3; i <= N; i++){
       f[i] = (f[i - 1] + f[i - 2]) % 10007;
   }

   cout << f[N];

}

#endif //ALGORITHM_11726_H
