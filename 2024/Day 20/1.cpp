#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
    Node* prev;
};

const int N = 15;
bool is_wall[N][N];
Node grid[N][N];

pair<int,int> start, finish;
pair<int,int> dirs[4] = { {-1,0}, {0,1}, {1,0}, {0,-1} };

bool comp(const pair<int,int>& a, const pair<int,int>& b) {
    const auto& [ai, aj] = a;
    const auto& [bi, bj] = b;
    return grid[ai][aj].g > grid[bi][bj].g;
}

priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(&comp)> unvisited(comp);

int main() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            char c = getchar();
            switch (c) {
                case '#':
                    is_wall[i][j] = true;
                    break;
                case 'S':
                    start = {i,j};
                    break;
                case 'E':
                    finish = {i,j};
                    break;
            }
            grid[i][j] = { INT_MAX, is_wall[i][j], NULL };
        }
        getchar();
    }

    grid[start.first][start.second].g = 0;
    unvisited.push(start);

    while (!unvisited.empty()) {
        const auto [ci,cj] = unvisited.top(); unvisited.pop();
        Node* curr = &grid[ci][cj];
        curr->visited = true;

        if (ci == finish.first && cj == finish.second) break; // found finish

        for (const auto [di,dj] : dirs) {
            const int ni = ci + di, nj = cj + dj;
            Node* next = &grid[ni][nj];

            if (next->visited) continue;

            int new_g = curr->g + 1;
            if (new_g < next->g) {
                next->g = new_g;
                next->prev = curr;
                unvisited.push({ni,nj});
            }
        }
    }

    cout << grid[finish.first][finish.second].g << '\n';
}
