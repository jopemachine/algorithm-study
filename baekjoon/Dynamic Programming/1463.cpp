/*
==============================+===============================================================
@ File Name : 1463.h
@ Author : jopemachine
@ Desc : 
@    1로 만들기
@    반복문을 돌면서 cache에 값들을 저장하면서 주어진 input 까지 반복문을 돌면 된다.
@    cache[2], cache[3]엔 직접 값을 넣어준다 (base case)
==============================+===============================================================
*/
#pragma once
// to use unsafe function
#pragma warning(disable: 4996)

#include <iostream>
#include <string>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <memory.h>

using namespace std;

int input;

int cache[1000001];

int main() {

	memset(cache, 0, sizeof(cache));
	cache[2] = 1;
	cache[3] = 1;

	// Prev Conv:: 1 <= N <= 10 ^ 6
	cin >> input;

	for (int i = 4; i <= input; i++) {
		
		if (i % 3 == 0 && i % 2 != 0) {
			cache[i] = min(cache[i - 1], cache[i / 3]) + 1;
		}
		else if (i % 3 != 0 && i % 2 == 0) {
			cache[i] = min(cache[i - 1], cache[i / 2]) + 1;
		}
		else if (i % 3 == 0 && i % 2 == 0) {
			cache[i] = min(min(cache[i / 3], cache[i / 2]), min(cache[i / 2], cache[i - 1])) + 1;
		}
		else {
			cache[i] = cache[i - 1] + 1;
		}
	}

	cout << cache[input];

}