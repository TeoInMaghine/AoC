#include <bits/stdc++.h>
using namespace std;

const int N = 130;
bool visited[N][N];
bool obstacles[N][N];
// Guard positions
int x, y;
// Cardinal directions: x1,y1,x2,y2, ...
int dirs[4*2] = {-1,0, 0,1, 1,0, 0,-1};

int main() {
    for (int i = 0; i < N; i++) {
        char c;
        for (int j = 0; j < N; j++) {
            scanf("%c", &c);
            if (c == '#')
                obstacles[i][j] = true;
            else if (c == '^') {
                y = i;
                x = j;
            }
        }
        scanf("%c", &c); // Skip \n
    }

    int dir_i = 0;

    while (true) {
        // cout << x << "," << y << endl;
        visited[y][x] = true;

        int diry = dirs[dir_i];
        int dirx = dirs[dir_i + 1];

        int newy = y + diry;
        int newx = x + dirx;

        if (newx >= N || newx < 0 || newy >= N || newy < 0) break;

        if (obstacles[newy][newx]) {
            dir_i = (dir_i + 2) % 8; // Rotate 90º
        } else { // Move
            y = newy;
            x = newx;
        }
    }

    int result = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            result += visited[i][j];
        }
    }

    cout << result << endl;
}

