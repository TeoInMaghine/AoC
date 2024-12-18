#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
};

const Node def = {INT_MAX, false};
const int N = 71;

Node grid[N][N];

pair<int,int> dirs[4] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

bool comp(const pair<int,int>& a, const pair<int,int>& b) {
    const auto& [ai, aj] = a;
    const auto& [bi, bj] = b;
    return grid[ai][aj].g > grid[bi][bj].g;
}

int main() {
    fill_n(&grid[0][0], N * N, def);

    for (int b = 0; b < 1024; b++) {
        char c;
        int i,j;
        scanf("%d", &j);
        scanf("%c", &c);
        scanf("%d", &i);
        scanf("%c", &c);

        grid[i][j].visited = true;
    }

    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < N; j++) {
    //         cout << (grid[i][j].visited ? '#' : '.');
    //     }
    //     cout << '\n';
    // }

    grid[0][0].g = 0;
    grid[0][0].visited = true;
    priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(&comp)> unvisited(&comp);
    unvisited.push({ 0, 0 });

    while (!unvisited.empty()) {
        const auto [i, j] = unvisited.top(); unvisited.pop();

        if (i == N-1 && j == N-1) break; // reached end

        Node* curr = &grid[i][j];
        curr->visited = true;

        for (const auto [di, dj] : dirs) {
            const int ni = i + di, nj = j + dj;
            if (ni < 0 || ni >= N || nj < 0 || nj >= N) continue;

            Node* next = &grid[ni][nj];
            if (next->visited) continue;

            int new_g = curr->g + 1;
            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push({ ni, nj });
            }
        }
    }

    cout << grid[N-1][N-1].g << '\n';
}
