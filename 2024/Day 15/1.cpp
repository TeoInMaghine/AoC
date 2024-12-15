#include <bits/stdc++.h>
using namespace std;

#define ll long long unsigned

enum Tile {Empty, Wall, Box};
const int N = 50;
Tile grid[N][N];
pair<int,int> bot;

const pair<int,int> U = {-1,0};
const pair<int,int> R = {0,1};
const pair<int,int> D = {1,0};
const pair<int,int> L = {0,-1};
vector<pair<int,int>> dirs;

int main() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            switch (getchar()) {
                case '.':
                    grid[i][j] = Empty;
                    break;
                case '#':
                    grid[i][j] = Wall;
                    break;
                case 'O':
                    grid[i][j] = Box;
                    break;
                default:
                    grid[i][j] = Empty;
                    bot = {i,j};
            }
        }
        // ignore newline
        getchar();
    }

    char c;
    while (scanf("%c", &c) != EOF) {
        switch (c) {
            case '^':
                dirs.push_back(U);
                break;
            case '>':
                dirs.push_back(R);
                break;
            case 'v':
                dirs.push_back(D);
                break;
            case '<':
                dirs.push_back(L);
                break;
        }
    }

    for (auto [di,dj] : dirs) {
        auto [bi,bj] = bot;

        deque<pair<int,int>> to_move = { bot };
        bool can_move = false;
        for (int i = bi + di, j = bj + dj; 
                i >= 0 && i < N && j >= 0 && j < N;
                i += di, j += dj) {
            switch (grid[i][j]) {
                case Empty:
                    can_move = true;
                    goto end;
                case Box:
                    to_move.push_front({i,j});
                    break;
                case Wall:
                    can_move = false;
                    goto end;
            }
        }
        end:
        if (can_move) {
            for (auto [i,j] : to_move) {
                int ni = i + di;
                int nj = j + dj;
                grid[ni][nj] = grid[i][j];
            }

            auto [i,j] = bot;
            i += di;
            j += dj;
            bot = {i,j};
            grid[i][j] = Empty;
        }
    }

    ll answer = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            // if (bot.first == i && bot.second == j) cout << '@';
            // else cout << (grid[i][j] == Empty ? '.' : grid[i][j] == Wall ? '#' : 'O');

            if (grid[i][j] == Box) {
                answer += 100 * i + j;
            }
        }
        // cout << '\n';
    }

    cout << answer << '\n';
}
