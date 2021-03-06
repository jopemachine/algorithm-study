/*
==============================+===============================================================
@ File Name : 11729_topOfHanoi.h
@ Author : jopemachine
@ Desc : 
@    ** Fail **
@    하노이 탑 이동 순서
==============================+===============================================================
*/
#pragma once

#include <iostream>
#include <stack>
#include <memory.h>
#include <cmath>


using namespace std;

void solve(int n, int source, int by, int dest) {
    if(n == 1){
        cout << source << " " << dest << "\n";
        return;
    }

    solve(n-1, source, dest , by);
    cout << source << " " << dest << "\n";
    solve(n-1, by, source, dest);
}


void other_solve_solution(int n, int x, int y) {
    if (n == 0) return;
    //x+y+z=6 - > 6-x-y = z;
    other_solve_solution(n - 1, x, 6 - x - y);

    printf("%d %d\n", x, y);
    other_solve_solution(n - 1, 6 - x - y, y);

}

int main(){
    int n;
    cin >> n;

    cout << (int) pow(2, n) - 1 << "\n";
    solve(n, 1, 2, 3);

    // solve_solution(n, 1, 3);
}