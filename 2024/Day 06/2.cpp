#include <bits/stdc++.h>
using namespace std;

const int N = 130;

bool visited[4][N][N];
bool obstacles[N][N];

// Cardinal directions: i1,j1, i2,j2, ...
int dirs[4*2] = {-1,0, 0,1, 1,0, 0,-1};


int rotated_90(int dir_i) {
    return (dir_i + 2) % 8;
}

bool try_cicle(int x, int y, int dir_i) {
    // Reset visited
    fill_n(&visited[0][0][0], 4 * N * N, false);

    // Add the obstacle if it wouldn't be outside bounds and doesn't exist already
    int obstacle_y = y + dirs[dir_i];
    int obstacle_x = x + dirs[dir_i + 1];
    if (obstacle_x >= N || obstacle_x < 0 || obstacle_y >= N || obstacle_y < 0 || obstacles[obstacle_y][obstacle_x])
        return false;
    obstacles[obstacle_y][obstacle_x] = true;

    visited[dir_i/2][y][x] = true;

    // Turn
    dir_i = rotated_90(dir_i);

    // cout << x << "," << y << " dir: " << dir_i << endl;
    while (true) {
        if (visited[dir_i/2][y][x]) {
            // Restore obstacles before returning
            obstacles[obstacle_y][obstacle_x] = false;
            // cout << "Yup" << endl;
            return true;
        }

        visited[dir_i/2][y][x] = true;

        int diry = dirs[dir_i];
        int dirx = dirs[dir_i + 1];

        int newy = y + diry;
        int newx = x + dirx;

        if (newx >= N || newx < 0 || newy >= N || newy < 0) break;

        if (obstacles[newy][newx]) {
            // Turn
            dir_i = rotated_90(dir_i);
        } else {
            // Move
            y = newy;
            x = newx;
        }
    }

    // Restore obstacles before returning
    obstacles[obstacle_y][obstacle_x] = false;
    return false;
}

int main() {
    // Guard starting position
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

    int result = 0;
    // Start upward
    int dir_i = 0;
    // Guard current position
    int x = original_x, y = original_y;
    while (true) {
        result += try_cicle(x, y, dir_i);

        int diry = dirs[dir_i];
        int dirx = dirs[dir_i + 1];

        int newy = y + diry;
        int newx = x + dirx;

        if (newx >= N || newx < 0 || newy >= N || newy < 0) break;

        if (obstacles[newy][newx]) {
            // Turn
            dir_i = rotated_90(dir_i);
        } else {
            // Move
            y = newy;
            x = newx;
        }
    }

    cout << result << endl;
}

