#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
    int i, j, d;

    // for tracking the best paths
    int prev_count = 0;
    Node* prevs[3];

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

        // advance
        const auto& [di, dj] = dirs[curr.d];
        const int ni = curr.i + di, nj = curr.j + dj;
        Node* next = &grid[ni][nj][curr.d];

        if (!next->visited) {
            int new_g = curr.g + 1;

            // track additional best path
            if (new_g == next->g) {
                next->prevs[next->prev_count] = &grid[curr.i][curr.j][curr.d];
                next->prev_count++;
            }

            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push(*next);

                // start tracking (new) best path
                next->prevs[0] = &grid[curr.i][curr.j][curr.d];
                next->prev_count = 1;
            }
        }

        // rotate 90º
        next = &grid[curr.i][curr.j][(curr.d + 1) % 4];

        if (!next->visited) {
            int new_g = curr.g + 1000;

            // track additional best path
            if (new_g == next->g) {
                next->prevs[next->prev_count] = &grid[curr.i][curr.j][curr.d];
                next->prev_count++;
            }

            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push(*next);

                // start tracking (new) best path
                next->prevs[0] = &grid[curr.i][curr.j][curr.d];
                next->prev_count = 1;
            }
        }

        // rotate -90º
        next = &grid[curr.i][curr.j][(curr.d + 3) % 4];

        if (!next->visited) {
            int new_g = curr.g + 1000;

            // track additional best path
            if (new_g == next->g) {
                next->prevs[next->prev_count] = &grid[curr.i][curr.j][curr.d];
                next->prev_count++;
            }

            if (new_g < next->g) {
                next->g = new_g;
                unvisited.push(*next);

                // start tracking (new) best path
                next->prevs[0] = &grid[curr.i][curr.j][curr.d];
                next->prev_count = 1;
            }
        }
    }

    int i = end->i, j = end->j;
    // max because I inverted the operator< lol
    int best_g = max({grid[i][j][0], grid[i][j][1], grid[i][j][2], grid[i][j][3]}).g;

    set<pair<int,int>> answer;
    vector<Node> currents;
    for (int d = 0; d < 4; d++)
        if (grid[i][j][d].g == best_g)
            currents.push_back(grid[i][j][d]);

    while (!currents.empty()) {
        Node current = currents.back(); currents.pop_back();
        answer.insert({current.i, current.j});

        for (int p = 0; p < current.prev_count; p++) {
            currents.push_back(*current.prevs[p]);
        }
    }

    cout << answer.size() << '\n';
}
