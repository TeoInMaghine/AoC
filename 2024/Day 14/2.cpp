#include <bits/stdc++.h>
using namespace std;

#define ll long long

const int H = 103, W = 101, INPUTS = 500;

int main() {
    tuple<int,int,int,int> inputs[INPUTS];

    char c[3];
    int i = 0;
    while (scanf("%c", c) != EOF) {

        int px, py, vx, vy;
        scanf("%c", c);
        scanf("%d", &px);
        scanf("%c", c);
        scanf("%d", &py);
        scanf("%3c", c);
        scanf("%d", &vx);
        scanf("%c", c);
        scanf("%d", &vy);
        scanf("%c", c);

        inputs[i] = {px,py,vx,vy};
        i++;
    }

    ll min_safety_factor = LONG_LONG_MAX;
    int min_s = 0;

    for (int s = 1; s < 1e5; s++) {
        int cuadrants[4] = {0, 0, 0, 0};
        for (auto [px,py,vx,vy] : inputs) {
            ll x = px + vx * s;
            ll y = py + vy * s;
            x = ((x % W) + W) % W;
            y = ((y % H) + H) % H;

            if (x < W / 2) {
                if (y < H / 2) cuadrants[0]++;
                else if (y > H / 2) cuadrants[1]++;
            } else if (x > W / 2) {
                if (y < H / 2) cuadrants[2]++;
                else if (y > H / 2) cuadrants[3]++;
            }
        }
        ll safety_factor = cuadrants[0] * cuadrants[1] * cuadrants[2] * cuadrants[3];

        if (safety_factor < min_safety_factor) {
            min_safety_factor = safety_factor;
            min_s = s;
        }
    }

    bool grid[H][W] = {false};
    int s = min_s;
    for (auto [px,py,vx,vy] : inputs) {
        ll x = px + vx * s;
        ll y = py + vy * s;
        x = ((x % W) + W) % W;
        y = ((y % H) + H) % H;

        grid[y][x] = true;
    }

    cout << "\nSECOND: " << s << "\n\n";
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cout << (grid[i][j] ? '@' : ' ');
        }
        cout << '\n';
    }
}
