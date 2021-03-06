/*
==============================+===============================================================
@ File Name : 9095.h
@ Author : jopemachine
@ Desc : 
@    ** Fail **
@    1, 2, 3 더하기
@ Ref URLs : 
@    https://nhs0912.tistory.com/62
==============================+===============================================================
*/

#ifndef ALGORITHM_9095_H
#define ALGORITHM_9095_H

#pragma once
// to use unsafe function
#pragma warning(disable: 4996)

#include <iostream>
#include <algorithm>
#include <array>

using namespace std;

int main(){

    int n;
    cin >> n;

    int* inputs = new int[n];
    // n < 11
    array<int, 11> cache;

    cache[1] = 1;
    cache[2] = 2;
    cache[3] = 4;

    int maxInput = 0;

    for(int i = 0; i < n; i++){
        cin >> inputs[i];
        if(inputs[i] > maxInput) maxInput = inputs[i];
    }

    for(int i = 4; i <= maxInput; i++){
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3];
    }

    for(int i = 0; i < n; i++){
        cout << cache[inputs[i]] << "\n";
    }

}


#endif //ALGORITHM_9095_H


