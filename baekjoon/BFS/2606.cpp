/*
==============================+===============================================================
@ File Name : 2606.h
@ Author : jopemachine
@ Desc : 
@    바이러스
@    BFS 문제. 노드들을 중복해 카운팅하지 않기 위해 linked란 vector<int>를 만들고 중복되면 linked에
@    넣지 않았다.
==============================+===============================================================
*/
#ifndef ALGORITHM_2606_H
#define ALGORITHM_2606_H

#include <algorithm>
#include <iostream>
#include <queue>
#include <memory.h>

using namespace std;

int main(){
    int N, Links;

    cin >> N;
    cin >> Links;

    int** map  = new int*[N];
    int** dist = new int*[N];

    for (int i = 0; i < N; i++){
        map[i]  = new int[N];
        dist[i] = new int[N];
        memset(map[i], 0, sizeof(int) * N);
        memset(dist[i], 0, sizeof(int) * N);
    }

    for (int i = 0; i < Links; i++){
        int    x,   y;
        cin >> x >> y;
        map[y-1][x-1] = 1;
        map[x-1][y-1] = 1;
    }

    // { first : dest, second : source }
    queue<int> que;
    vector<int> linked;

    que.push(0);

    while(!que.empty()){

        int px  = que.front();

        for(int i = 1; i < N; i++){
            if(map[i][px] == 1 && dist[i][px] == 0 && dist[px][i] == 0){
                que.push(i);
                dist[i][px] = 1;
                dist[px][i] = 1;
                if(linked.end() == find(linked.begin(), linked.end(), i)){
                    linked.push_back(i);
                }
            }

        }
        que.pop();
    }

    cout << linked.size();

}

#endif //ALGORITHM_2606_H
