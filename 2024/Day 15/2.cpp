#include <bits/stdc++.h>
using namespace std;

#define ll long long unsigned

enum Tile {Empty, Wall, LBox, RBox};
const int N = 50;
Tile previous[N][2*N];
Tile current[N][2*N];

pair<int,int> bot;

const pair<int,int> U = {-1,0};
const pair<int,int> R = {0,1};
const pair<int,int> D = {1,0};
const pair<int,int> L = {0,-1};
vector<pair<int,int>> dirs;

deque<pair<int,int>> to_move = { };

bool can_move(int i, int j, int di, int dj) {
    int ni = i + di, nj = j + dj;
    // I don't think this will ever happen but just in case...
    if (ni < 0 || ni >= N || nj < 0 || nj >= 2*N) return false;

    switch (previous[i][j]) {
        case Wall:
            return false;
        case Empty:
            return true;
        case LBox:
            if (di != 0) { // If moving vertically:
                to_move.push_front({i,j});
                to_move.push_front({i,j+1});
                return can_move(ni, nj, di, dj) && can_move(ni, nj+1, di, dj);
            } else { // Otherwise avoid infinite recursion:
                to_move.push_front({i,j});
                return can_move(ni, nj, di, dj);
            }
        case RBox:
            if (di != 0) { // If moving vertically:
                to_move.push_front({i,j});
                to_move.push_front({i,j-1});
                return can_move(ni, nj-1, di, dj) && can_move(ni, nj, di, dj);
            } else { // Otherwise avoid infinite recursion:
                to_move.push_front({i,j});
                return can_move(ni, nj, di, dj);
            }
    }

    // Shouldn't ever reach here
    assert(false);
    return false;
}

int main() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            switch (getchar()) {
                case '.':
                    previous[i][2*j] = Empty;
                    previous[i][2*j+1] = Empty;
                    current[i][2*j] = Empty;
                    current[i][2*j+1] = Empty;
                    break;
                case '#':
                    previous[i][2*j] = Wall;
                    previous[i][2*j+1] = Wall;
                    current[i][2*j] = Wall;
                    current[i][2*j+1] = Wall;
                    break;
                case 'O':
                    previous[i][2*j] = LBox;
                    previous[i][2*j+1] = RBox;
                    current[i][2*j] = LBox;
                    current[i][2*j+1] = RBox;
                    break;
                default:
                    previous[i][2*j] = Empty;
                    previous[i][2*j+1] = Empty;
                    current[i][2*j] = Empty;
                    current[i][2*j+1] = Empty;
                    bot = {i,2*j};
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

        if (can_move(bi + di, bj + dj, di, dj)) {
            // to avoid having to be careful about movement order,
            // I use 2 different grids

            // first, "clean" current grid
            for (auto [i,j] : to_move) {
                current[i][j] = Empty;
            }

            // then, "move" from previous to current
            for (auto [i,j] : to_move) {
                int ni = i + di;
                int nj = j + dj;
                current[ni][nj] = previous[i][j];
            }

            // finally, "copy" current to previous
            for (auto [i,j] : to_move) {
                int ni = i + di;
                int nj = j + dj;
                previous[i][j] = current[i][j];
                previous[ni][nj] = current[ni][nj];
            }

            // by this point, current and previous have the same values

            auto [i,j] = bot;
            i += di;
            j += dj;
            bot = {i,j};
        }

        to_move.clear();
    }

    ll answer = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 2*N; j++) {
            if (current[i][j] == LBox) {
                answer += 100 * i + j;
            }
        }
    }

    cout << answer << '\n';
}
