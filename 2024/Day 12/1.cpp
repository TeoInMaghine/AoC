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
    int area = 0, perimeter = 0;
    char type = grid[start_i][start_j];

    // container with new nodes of the region
    deque<pair<int,int>> new_nodes;
    new_nodes.push_back({start_i, start_j});
    visited[start_i][start_j] = true;

    while (!new_nodes.empty()) {
        auto [i,j] = new_nodes.front();
        new_nodes.pop_front();
        area++;

        for (auto [dir_i, dir_j] : dirs) {
            int new_i = i + dir_i;
            int new_j = j + dir_j;

            // count borders
            if (!is_in_grid(new_i, new_j) || grid[new_i][new_j] != type) {
                perimeter++;
                continue;
            }
            
            if (visited[new_i][new_j]) continue;

            new_nodes.push_back({new_i, new_j});
            visited[new_i][new_j] = true;
        }
    }

    return area * perimeter;
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
