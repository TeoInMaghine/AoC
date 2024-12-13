#include <bits/stdc++.h>
using namespace std;

#define ll long long unsigned

const int N = 140;
bool visited[N][N];

pair<int,int> dirs[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
vector<string> grid;


bool is_in_grid(int i, int j) {
    return i >= 0 && i < N && j >= 0 && j < N;
}

ll floodfill(int start_i, int start_j) {
    int area = 0, sides = 0;
    char type = grid[start_i][start_j];

    // container with new nodes of the region
    deque<pair<int,int>> new_nodes;
    // grid with borders and their set directions
    // size N+2 to account for -1 and N indices
    bool borders[4][N+2][N+2];
    fill_n(&borders[0][0][0], 4 * (N+2) * (N+2), false);

    new_nodes.push_back({start_i, start_j});
    visited[start_i][start_j] = true;

    while (!new_nodes.empty()) {
        auto [i,j] = new_nodes.front();
        new_nodes.pop_front();
        area++;

        for (int d = 0; d < 4; d++) {
            auto [dir_i, dir_j] = dirs[d];

            int new_i = i + dir_i;
            int new_j = j + dir_j;

            // count borders
            if (!is_in_grid(new_i, new_j) || grid[new_i][new_j] != type) {
                // add 1 to the coordinates to account for -1 indices
                borders[d][new_i+1][new_j+1] = true;
                continue;
            }
            
            if (visited[new_i][new_j]) continue;

            new_nodes.push_back({new_i, new_j});
            visited[new_i][new_j] = true;
        }
    }

    for (int d = 0; d < 4; d++) {
        for (int i = 0; i < N+2; i++) {
            for (int j = 0; j < N+2; j++) {
                if (borders[d][i][j]) {
                    // sides have two vertices, so I count half of those
                    auto perpendicular_dir = dirs[(d+1) % 4];
                    auto [di, dj] = perpendicular_dir;
                    bool is_vertice = !borders[d][i + di][j + dj];
                    sides += is_vertice;
                }
            }
        }
    }

    return area * sides;
}

int main() {
    string s;
    while (getline(cin, s)) {
        grid.push_back(s);
    }

    ll answer = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j])
                answer += floodfill(i, j);
        }
    }

    cout << answer << endl;
}
