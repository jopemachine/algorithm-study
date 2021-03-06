/*
==============================+===============================================================
@ File Name : 2905_paintPlane.h
@ Author : jopemachine
@ Desc : 
@    ** Fail **
@ Ref URLs : 
@    https://jaimemin.tistory.com/832
==============================+===============================================================
*/

#ifndef ALGORITHM_2905_PAINTPLANE_H
#define ALGORITHM_2905_PAINTPLANE_H

#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main() {

    int heightNumber;

    int brushWidth;
    cin >> heightNumber >> brushWidth;

    int* heightInputs = new int[heightNumber];

    for(int i = 0; i < heightNumber; i++){
        cin >> heightInputs[i];
    }

    int planeNumber;

    if(heightNumber % brushWidth == 0){
        planeNumber = heightNumber / brushWidth;
    }
    else{
        if(heightNumber < brushWidth){
            planeNumber = 0;
        }
        else{
            planeNumber = (heightNumber / brushWidth) + 1;
        }
    }



}



#endif //ALGORITHM_2905_PAINTPLANE_H
