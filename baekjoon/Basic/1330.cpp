/*
==============================+===============================================================
@ File Name : 1330.h
@ Author : jopemachine
==============================+===============================================================
*/
#ifndef ALGORITHM_1330_H
#define ALGORITHM_1330_H

#include <iostream>
using namespace std;

int main(){
    int A, B;

    cin >> A >> B;

    if(A == B) cout << "==";
    else if(A > B) cout << ">";
    else cout << "<";
}

#endif //ALGORITHM_1330_H
