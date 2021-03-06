/*
==============================+===============================================================
@ File Name : 11403_searchPath.h
@ Author : jopemachine
@ Desc : 
@    경로 찾기
@    풀다 만 문제.
==============================+===============================================================
*/
#pragma once
// to use unsafe function
#pragma warning(disable: 4996)

#include <iostream>
#include <string>
#include <stdlib.h>
#include <queue>
#include <stack>

using namespace std;

int map_size;

int** map;
int** solution;
int** visitedPlace;

stack<int> path_stack;

void search_pathExist_recursive(int dest, int start, int col) {

	if (map[col][dest] == 1) {
		solution[start][dest] = 1;
		return;
	}
	for (int row = 0; row < map_size; row++) {

		if (map[col][row] != 1) {
			continue;
		}

		if (visitedPlace[col][row] == 1) {
			return;
		}

		visitedPlace[col][row] = 1;
		search_pathExist_recursive(dest, start, row);

	}
}

int main() {

	// Prev Cond:: 1 <= N <= 100
	cin >> map_size;

	map = new int* [map_size];
	solution = new int* [map_size];
	visitedPlace = new int* [map_size];

	for (int i = 0; i < map_size; i++) {
		map[i] = new int[map_size];
		solution[i] = new int[map_size];
		visitedPlace[i] = new int[map_size];
		memset(map[i], 0, sizeof(int) * map_size);
		memset(solution[i], 0, sizeof(int) * map_size);
		memset(visitedPlace[i], 0, sizeof(int) *map_size);
	}

	for (int i = 0; i < map_size; i++) {
		for (int j = 0; j < map_size; j++) {
			cin >> map[i][j];
		}
	}

	for (int i = 0; i < map_size; i++) {
		for (int j = 0; j < map_size; j++) {
			search_pathExist_recursive(j, i, i);
			for (int i = 0; i < map_size; i++) {
				memset(visitedPlace[i], 0, sizeof(int) * map_size);
			}
		}
	}

	for (int i = 0; i < map_size; i++) {
		for (int j = 0; j < map_size; j++) {
			cout << solution[i][j] << " ";
		}
		cout << "\n";
	}
	
}