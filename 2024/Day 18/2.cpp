#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
};

const int N = 71;
Node grid[N][N];

pair<int,int> dirs[4] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

bool comp(const pair<int,int>& a, const pair<int,int>& b) {
    const auto& [ai, aj] = a;
    const auto& [bi, bj] = b;
    return grid[ai][aj].g > grid[bi][bj].g;
}

priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(&comp)> unvisited(&comp);

bool pathfinding() {

    while (!unvisited.empty()) {
        const auto [i, j] = unvisited.top(); unvisited.pop();

        if (i == N-1 && j == N-1) return true; // reached end

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

    return false;
}

int main() {
    const Node def = {INT_MAX, false};
    fill_n(&grid[0][0], N * N, def);

    pair<int,int> bytes[3450];
    for (int b = 0; b < 3450; b++) {
        char c;
        int i,j;
        scanf("%d", &j);
        scanf("%c", &c);
        scanf("%d", &i);
        scanf("%c", &c);

        bytes[b] = {i, j};
        grid[i][j].visited = true;
    }

    grid[0][0].g = 0;
    grid[0][0].visited = true;
    unvisited.push({ 0, 0 });
    pathfinding();

    // go through obstacle positions in reverse order,
    // removing them instead of adding them, and only try
    // pathfinding when the obstacle could've been blocking
    // a path
    int i, j;
    for (int b = 3450; b >= 0; b--) {
        i = bytes[b].first;
        j = bytes[b].second;
        grid[i][j].visited = false;

        // see if any neighbour has been part of the search,
        // if so than this position could be in the path to the end
        for (const auto [di, dj] : dirs) {
            const int ni = i + di, nj = j + dj;
            if (ni < 0 || ni >= N || nj < 0 || nj >= N) continue;

            Node* next = &grid[ni][nj];
            if (next->g != INT_MAX) {
                grid[i][j].g = 0;
                unvisited.push({ i, j });
                if (pathfinding()) goto end;
                break;
            }
        }
    }
    end:
    cout << j << "," << i << '\n';
}
