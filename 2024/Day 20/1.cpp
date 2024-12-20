#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
    pair<int,int> prev;
};

const int N = 141;
const pair<int,int> dirs[4] = { {-1,0}, {0,1}, {1,0}, {0,-1} };
const pair<int,int> cheat_offsets[8] = { {-2,0}, {-1,1}, {0,2}, {1,1}, {2,0}, {1,-1}, {0,-2}, {-1,-1} };

Node grid[N][N];

bool comp(const pair<int,int>& a, const pair<int,int>& b) {
    const auto& [ai, aj] = a;
    const auto& [bi, bj] = b;
    return grid[ai][aj].g > grid[bi][bj].g;
}

priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(&comp)> unvisited(comp);

pair<int,int> start, finish;
set<pair<int,int>> path;
// seconds saved: # of cheats
map<int,int> cheat_saves;

int main() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            bool is_wall = false;
            switch (getchar()) {
                case '#':
                    is_wall = true;
                    break;
                case 'S':
                    start = {i,j};
                    break;
                case 'E':
                    finish = {i,j};
                    break;
            }
            grid[i][j] = { INT_MAX, is_wall, {-1,-1} };
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

        for (const auto& [di,dj] : dirs) {
            const int ni = ci + di, nj = cj + dj;
            Node* next = &grid[ni][nj];

            if (next->visited) continue;

            int new_g = curr->g + 1;
            if (new_g < next->g) {
                next->g = new_g;
                next->prev = {ci,cj};
                unvisited.push({ni,nj});
            }
        }
    }

    pair<int,int> curr = finish;
    do {
        path.insert(curr);
        curr = grid[curr.first][curr.second].prev;
    } while (curr.first != -1 && curr.second != -1);

    for (const auto& [i,j] : path) {
        const int curr = grid[i][j].g;

        for (const auto& [di,dj] : cheat_offsets) {
            const int ni = i + di, nj = j + dj;

            if (path.contains({ni,nj})) {
                const int& next = grid[ni][nj].g;
                int seconds_saved = next - curr - 2;

                if (seconds_saved > 0)
                    cheat_saves[seconds_saved]++;
            }
        }
    }

    int answer = 0;
    for (auto it = cheat_saves.lower_bound(100); it != cheat_saves.end(); ++it) {
        answer += it->second;
    }

    cout << answer << '\n';
}
