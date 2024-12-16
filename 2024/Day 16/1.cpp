#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
    int i, j, d;

    // for the min-priority queue
    bool operator<(const Node& right) const {
        return g > right.g;
    }
};

// E, S, W, N
const pair<int,int> dirs[4] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
const int N = 141;

Node grid[N][N][4];
priority_queue<Node> unvisited;

int main() {
    // the end is only to save the i and j coordinates really
    Node *start, *end;

    for (int i = 0; i < N; i++) {
        char c;
        Node node;
        for (int j = 0; j < N; j++) {
            scanf("%c", &c);
            for (int d = 0; d < 4; d++) {
                node = { INT_MAX, c == '#', i, j, d };
                grid[i][j][d] = node;
                if (c == 'S' && d == 0) start = &grid[i][j][d];
                if (c == 'E' && d == 0) end = &grid[i][j][d];
            }
        }
        scanf("%c", &c); // ignore '\n'
    }

    start->g = 0;
    unvisited.push(*start);
    
    while (!unvisited.empty()) {
        const Node curr = unvisited.top(); unvisited.pop();
        grid[curr.i][curr.j][curr.d].visited = true;

        if (curr.i == end->i && curr.j == end->j) break;

        // advance
        const auto& [di, dj] = dirs[curr.d];
        const int ni = curr.i + di, nj = curr.j + dj;
        Node* next = &grid[ni][nj][curr.d];

        if (!next->visited) {
            int new_g = curr.g + 1;
            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push(*next);
            }
        }

        // rotate 90º
        next = &grid[curr.i][curr.j][(curr.d + 1) % 4];

        if (!next->visited) {
            int new_g = curr.g + 1000;
            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push(*next);
            }
        }

        // rotate -90º
        next = &grid[curr.i][curr.j][(curr.d + 3) % 4];

        if (!next->visited) {
            int new_g = curr.g + 1000;
            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push(*next);
            }
        }
    }

    int i = end->i, j = end->j;
    // max because I inverted the operator< lol
    cout << max({grid[i][j][0], grid[i][j][1], grid[i][j][2], grid[i][j][3]}).g << '\n';
}
