/*
==============================+===============================================================
@ File Name : 2439.h
@ Author : jopemachine
==============================+===============================================================
*/
#ifndef ALGORITHM_2439_H
#define ALGORITHM_2439_H

#include <iostream>

using namespace std;

int main() {

    int N;
    cin >> N;
    int i = 1;
    while (N > 0) {

        for (int j = 0; j < N - 1; j++) cout << " ";
        for (int j = 0; j < i; j++)     cout << "*";

        cout << "\n";

        ++i; --N;
    }
}


#endif //ALGORITHM_2439_H
