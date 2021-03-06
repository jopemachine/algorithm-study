/*
==============================+===============================================================
@ File Name : 1065.h
@ Author : jopemachine
@ Desc : 
@    한수
@    단순한 brute force 문제.
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
int targetNumber = 0;

int main() {

	// Prev Cond:: 1<= N <= 1000
	cin >> input;

	for (int i = 1; i <= input; i++) {

		if (i < 100) {
			targetNumber++;
			continue;
		}

		int div1 = i % 10;
		int div2 = (i % 100) / 10;
		int div3 = i / 100;

		if (div3 - div2 == div2 - div1) {
			targetNumber++;
		}
	}

	cout << targetNumber;
		
}