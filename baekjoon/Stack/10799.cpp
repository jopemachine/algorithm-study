/*
==============================+===============================================================
@ File Name : 10799.h
@ Author : jopemachine
@ Desc : 
@    ** Fail **
@    쇠막대기
@    발상의 전환이 필요했던 문제. 아무리 생각해도 코드가 안 나와 구글에 검색해보고야
@    풀 수 있었다.
==============================+===============================================================
*/

#pragma once
// to use unsafe function
#pragma warning(disable: 4996)

#include <iostream>
#include <string>
#include <stack>

using namespace std;

string input;
stack<char> stk;

int result = 0;


int main() {

	cin >> input;

	for (int i = 0; i < input.size(); i++) {
		if (input[i] == '(') {
			stk.push('(');
		}
		else {
			if (input[i-1] =='(') {
				stk.pop();
				result += stk.size();
			}
			else {
				stk.pop();
				result += 1;
			}
		}
	}
	cout << result;
}
