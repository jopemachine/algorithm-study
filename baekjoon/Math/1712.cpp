#include <iostream>

using namespace std;

int main(){

    long A, B, C;

    cin >> A >> B >> C;

    int t = -1;
    if (B < C){
        t = (A / (C - B)) + 1;
    }

    cout << t;

}
