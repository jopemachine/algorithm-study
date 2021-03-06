/*
==============================+===============================================================
@ File Name : 9012_Parentheses.h
@ Author : jopemachine
@ Desc : 
@    괄호
==============================+===============================================================
*/
#pragma once
// to use unsafe function
#pragma warning(disable: 4996)

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int stringNumber;
stack<char> charStack;
string* str;

int main() {

	ios::sync_with_stdio(false);

	cin >> stringNumber;

	str = new string[stringNumber];

	string result = "";

	for (int i = 0; i < stringNumber; i++) {
		cin >> str[i];
	}

	bool f = false;

	for (int i = 0; i < stringNumber; i++) {

		f = false;
		
		for (int j = 0; j < str[i].size(); j++) {
			if (charStack.empty() && str[i].at(j) == ')') {
				result += "NO\n";
				f = true;
				break;
			}
			if (charStack.empty() || (charStack.top() == '(' && str[i].at(j) == '(')) {
				charStack.push(str[i].at(j));
			}
			else {
				charStack.pop();
			}
		}

		if (!charStack.empty() && !f) {
			result += "NO\n";
		}
		else if (charStack.empty() && !f){
			result += "YES\n";
		}

		while (!charStack.empty()) charStack.pop();
	}

	cout << result;

}
