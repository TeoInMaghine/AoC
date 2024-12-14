#include <bits/stdc++.h>
using namespace std;

const int H = 103, W = 101, SECS = 1;

int main() {
    int cuadrants[4] = {0, 0, 0, 0};

    char c[3];
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

        px += vx * SECS;
        py += vy * SECS;
        px = ((px % W) + W) % W;
        py = ((py % H) + H) % H;

        if (px < W / 2) {
            if (py < H / 2) cuadrants[0]++;
            else if (py > H / 2) cuadrants[1]++;
        } else if (px > W / 2) {
            if (py < H / 2) cuadrants[2]++;
            else if (py > H / 2) cuadrants[3]++;
        }
    }

    cout << cuadrants[0] * cuadrants[1] * cuadrants[2] * cuadrants[3] << '\n';
}
