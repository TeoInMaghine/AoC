#include <bits/stdc++.h>
using namespace std;

struct Node {
    int g;
    bool visited;
    pair<int,int> prev;
};

const int L = 9465;
const int N = 141;
const pair<int,int> dirs[4] = { {-1,0}, {0,1}, {1,0}, {0,-1} };

Node grid[N][N];

bool comp(const pair<int,int>& a, const pair<int,int>& b) {
    const auto& [ai, aj] = a;
    const auto& [bi, bj] = b;
    return grid[ai][aj].g > grid[bi][bj].g;
}

priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(&comp)> unvisited(comp);

pair<int,int> start, finish;
pair<int,int> path[L];
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

    int i = L-1;
    pair<int,int> curr = finish;
    do {
        path[i] = curr;
        curr = grid[curr.first][curr.second].prev;
        i--;
    } while (curr.first != -1 && curr.second != -1);

    int answer = 0;
    for (i = 0; i < L; i++) {
        const auto& [ci,cj] = path[i];
        for (int j = i+100; j < L; j++) {
            const auto& [ni,nj] = path[j];
            int dst = abs(ci - ni) + abs(cj - nj);
            answer += dst <= 20 && j - i >= dst + 99;
        }
    }

    cout << answer << '\n';
}
