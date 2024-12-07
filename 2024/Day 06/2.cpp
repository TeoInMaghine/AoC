#include <bits/stdc++.h>
using namespace std;

const int N = 10;

bool visited[N][N];
bool obstacles[N][N];
// Guard positions
int x, y;

// Indices of cardinal directions
const int U_I = 0;
const int R_I = 2;
const int D_I = 4;
const int L_I = 6;
// Cardinal directions: i1,j1, i2,j2, ...
int dirs[4*2] = {-1,0, 0,1, 1,0, 0,-1};

int r[N];
int d[N];
int l[N];
int u[N];

int rotate_90(int dir_i) {
    return (dir_i + 2) % 8;
}

int main() {
    // neutral elements -> -inf
    fill(r, r + N, INT_MIN);
    fill(d, d + N, INT_MIN);
    // neutral elements -> +inf
    fill(l, l + N, INT_MAX);
    fill(u, u + N, INT_MAX);

    int original_y, original_x;
    for (int i = 0; i < N; i++) {
        char c;
        for (int j = 0; j < N; j++) {
            scanf("%c", &c);
            if (c == '#')
                obstacles[i][j] = true;
            else if (c == '^') {
                original_y = i;
                original_x = j;
            }
        }
        scanf("%c", &c); // Skip \n
    }

    y = original_y;
    x = original_x;
    int dir_i = U_I;
    while (true) {

        int diry = dirs[dir_i];
        int dirx = dirs[dir_i + 1];

        int newy = y + diry;
        int newx = x + dirx;

        if (newx >= N || newx < 0 || newy >= N || newy < 0) break;

        // Hay lo que llamo un "endpoint"
        if (obstacles[newy][newx]) {
            switch (dir_i) {
                case R_I:
                    r[y] = max(r[y], x);
                    break;
                case D_I:
                    d[x] = max(d[x], y);
                    break;
                case L_I:
                    l[y] = min(l[y], x);
                    break;
                case U_I:
                    u[x] = min(u[x], y);
                    break;
            }

            dir_i = rotate_90(dir_i);
        } else { // Move
            y = newy;
            x = newx;
        }
    }

    int boxes = 0;
    y = original_y;
    x = original_x;
    dir_i = U_I;
    while (true) {

        cout << x << "," << y << endl;
        visited[y][x] = true;
        int eval_dir_i = rotate_90(dir_i);
        switch (eval_dir_i) {
            case R_I:
                boxes += x <= r[y];
                break;
            case D_I:
                boxes += y <= d[x];
                break;
            case L_I:
                boxes += x >= l[y];
                break;
            case U_I:
                boxes += y >= u[x];
                break;
        }


        int diry = dirs[dir_i];
        int dirx = dirs[dir_i + 1];

        int newy = y + diry;
        int newx = x + dirx;

        if (newx >= N || newx < 0 || newy >= N || newy < 0) break;

        // Hay lo que llamo un "endpoint"
        if (obstacles[newy][newx]) {
            dir_i = rotate_90(dir_i);
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

    cout << boxes << endl;
}

