#include <bits/stdc++.h>
using namespace std;

const int W = 5, H = 7;
// heights from top to bottom where
//    the solid ends:
vector<array<int,W>> locks;
//    the solid starts:
vector<array<int,W>> keys;

void parse_grid(string grid[H]) {
    array<int,W> heights = {0};

    const bool is_lock = grid[0][0] == '#';
    for (int j = 0; j < W; j++) {
        for (int i = 1; i < H; i++) {
            if (is_lock && grid[i][j] == '.') {
                heights[j] = i - 1;
                break;
            }

            if (!is_lock && grid[i][j] == '#') {
                heights[j] = i;
                break;
            }
        }
    }

    if (is_lock) locks.push_back(heights);
    else keys.push_back(heights);
}

int main() {
    string s;
    string grid[H];
    int i = 0;
    while (getline(cin, s)) {
        if (s.size() == 0) {
            parse_grid(grid);
            i = 0;
        } else {
            grid[i] = s;
            i++;
        }
    }
    parse_grid(grid);

    long answer = 0;
    for (const auto& key : keys) {
        for (const auto& lock : locks) {
            bool fits = true;
            for (int i = 0; i < W; i++) {
                if (lock[i] >= key[i]) {
                    fits = false;
                    break;
                }
            }
            answer += fits;
        }
    }

    cout << answer << '\n';
}
