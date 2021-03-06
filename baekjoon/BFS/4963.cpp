/*
==============================+===============================================================
@ File Name : 4963_numberOfIsland.h
@ Author : jopemachine
@ Desc : 
@    섬의 개수
@    BFS로 간단하게 풀 수 있는 문제. 대각선까지 고려해야하므로 8개 방향으로 모두 완전탐색해야 한다.
==============================+===============================================================
*/

#ifndef SELFMADE_ALGORITHM_4963_NUMBEROFISLAND_H
#define SELFMADE_ALGORITHM_4963_NUMBEROFISLAND_H

using namespace std;

#include <iostream>
#include <queue>
#include <memory.h>

// 0 <= w, h <= 50
int W, H;

int islandNumber = 0;
vector<int> islandNumbers;
queue<pair<int, int>> que;

bool solve_byBFS(pair<int, int> startVertex, int** map, int** dist){

    if(map[startVertex.second][startVertex.first] != 1 || dist[startVertex.second][startVertex.first] != -1){
        return false;
    }

    dist[startVertex.second][startVertex.first] = 1;

    que.push(startVertex);

    while(que.size() > 0){

        int row = que.front().first;
        int col = que.front().second;

        if ((row + 1 < W && row >= 0) && map[col][row + 1] == 1 && dist[col][row + 1] < 0) {
            que.push(make_pair(row + 1, col));
            dist[col][row + 1] = dist[col][row] + 1;
        }

        if ((col + 1 < H && col >= 0) && map[col + 1][row] == 1 && dist[col + 1][row] < 0) {
            que.push(make_pair(row, col + 1));
            dist[col + 1][row] = dist[col][row] + 1;
        }

        if (row - 1 >= 0 && map[col][row - 1] == 1 && dist[col][row - 1] < 0) {
            que.push(make_pair(row - 1, col));
            dist[col][row - 1] = dist[col][row] + 1;
        }

        if (col - 1 >= 0 && map[col - 1][row] == 1 && dist[col - 1][row] < 0) {
            que.push(make_pair(row, col - 1));
            dist[col - 1][row] = dist[col][row] + 1;
        }


        if(col - 1 >= 0 && (row + 1 < W && row >= 0) && map[col - 1][row + 1] == 1 && dist[col - 1][row + 1] < 0){
            que.push(make_pair(row + 1, col - 1));
            dist[col - 1][row + 1] = dist[col][row] + 1;
        }


        if((col + 1 < H && col >= 0) && (row + 1 < W && row >= 0) && map[col + 1][row + 1] == 1 && dist[col + 1][row + 1] < 0){
            que.push(make_pair(row + 1, col + 1));
            dist[col + 1][row + 1] = dist[col][row] + 1;
        }

        if((col + 1 < H && col >= 0) && row - 1 >= 0 && map[col + 1][row - 1] == 1 && dist[col + 1][row - 1] < 0){
            que.push(make_pair(row - 1, col + 1));
            dist[col + 1][row - 1] = dist[col][row] + 1;
        }

        if(col - 1 >= 0 && row - 1 >= 0 && map[col - 1][row - 1] == 1 && dist[col - 1][row - 1] < 0){
            que.push(make_pair(row - 1, col - 1));
            dist[col - 1][row - 1] = dist[col][row] + 1;
        }

        que.pop();
    }

    return true;
}

int main(){

    bool end = false;

    while(true){

        int** dist;
        int** map;

        cin >> W >> H;

        if(W == 0 && H == 0){
            break;
        }

        map  = new int*[H];
        dist = new int*[H];

        for(int i = 0; i < H; i++){
            map[i] = new int[W];
            dist[i] = new int[W];
            memset(map[i], 0, sizeof(int) * W);
            memset(dist[i], -1, sizeof(int) * W);
        }

        for (int i = 0; i < H; i++){
            for (int j = 0; j < W; j++){
                cin >> map[i][j];
            }
        }

        for (int i = 0; i < H; i++){
            for (int j = 0; j < W; j++){
                if(solve_byBFS({j, i}, map, dist)){
                    islandNumber++;
                };
            }
        }

        islandNumbers.push_back(islandNumber);
        islandNumber = 0;

        for(int k = 0; k < H; k++){
            memset(dist[k], -1, sizeof(int) * W);
        }

    }

    for(int i = 0; i < islandNumbers.size(); i++){
        cout << islandNumbers[i] << "\n";
    }
}
#endif //SELFMADE_ALGORITHM_4963_NUMBEROFISLAND_H
