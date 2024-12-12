#include <bits/stdc++.h>
using namespace std;

const int N = 47;
int grid[N][N];

// N, E, S, W
pair<int,int> dirs[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

bool in_grid(int i, int j) {
    return i >= 0 && i < N && j >= 0 && j < N;
}

uint get_goals_reachable(int i, int j) {
    if (grid[i][j] == 9) {
        return 1;
    }

    uint total = 0;

    // Iterate through neighbours
    for (auto dir : dirs) {
        int ni = i + dir.first;
        int nj = j + dir.second;

        if (in_grid(ni, nj) && grid[i][j] + 1 == grid[ni][nj]) {
            total += get_goals_reachable(ni, nj);
        }
    }

    return total;
}

int main() {

    char c;
    int i = 0, j = 0;
    while (scanf("%c", &c) != EOF) {
        if (c == '\n') {
            i++;
            j = 0;
        } else {
            grid[i][j] = c - '0';
            j++;
        }
    }

    uint answer = 0;

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (grid[i][j] == 0) {
                answer += get_goals_reachable(i,j);
            }
        }
    }

    cout << answer << endl;
}

