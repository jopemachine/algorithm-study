/*
==============================+===============================================================
@ File Name : 2630.h
@ Author : jopemachine
@ Desc : 
@    색종이 만들기
@    간단한 분할정복 문제.
==============================+===============================================================
*/

#ifndef ALGORITHM_2630_H
#define ALGORITHM_2630_H


#include <iostream>
#include <memory.h>

using namespace std;

int** map;

int blue  = 0;
int white = 0;

void divide(int** map, int begin_x, int end_x, int begin_y, int end_y){

    int hits_blue  = 0;
    int hits_white = 0;

    for (int y = begin_y; y <= end_y; y++){
        for (int x = begin_x; x <= end_x; x++){
                if(hits_blue != 0 && hits_white != 0) goto recur;
                if(map[y][x] == 1) hits_blue ++;
                else               hits_white++;
        }
    }

recur:

    // All white
    if(hits_blue == 0){
        white++;
    }
    // All blue
    else if(hits_white == 0){
        blue++;
    }
    // divide by recursive
    else{
        divide(map,  begin_x                   , (begin_x + end_x) / 2, begin_y                    , (begin_y + end_y) / 2);

        divide(map, ((begin_x + end_x) / 2) + 1, end_x                , begin_y                    , (begin_y + end_y) / 2);

        divide(map,  begin_x                   , (begin_x + end_x) / 2, ((begin_y + end_y) / 2 + 1), end_y    );

        divide(map, ((begin_x + end_x )/ 2) + 1, end_x                , ((begin_y + end_y) / 2 + 1), end_y    );
    }
}

int main(){

    int N;
    cin >> N;

    map = new int* [N];

    for(int i = 0; i < N; i++){
        map[i] = new int[N];
        memset(map[i], 0, sizeof(int) * N);
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
        }
    }

    divide(map, 0, N - 1, 0, N - 1);

    printf("%d\n%d", white, blue);
};



#endif //ALGORITHM_2630_H
