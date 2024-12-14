#include <bits/stdc++.h>
using namespace std;

#define ll long long

ll minimum_tokens(int ax, int ay, int bx, int by, ll px, ll py) {

    int determinant = ax*by - bx*ay;
    ll a_numerator = px*by - bx*py;
    ll b_numerator = ax*py - ay*px;
    if (a_numerator % determinant == 0 && b_numerator % determinant == 0) {
        ll a = a_numerator / determinant;
        ll b = b_numerator / determinant;
        return 3*a + b;
    }

    return 0;
}

int main() {
    ll answer = 0;

    char c;
    do {
        int ax, ay, bx, by, px, py;

        // "Button A: X+"
        for (int i = 0; i < 12; i++) getchar();
        scanf("%d", &ax);
        // ", Y+"
        for (int i = 0; i < 4; i++) getchar();
        scanf("%d", &ay);

        // "\nButton B: X+"
        for (int i = 0; i < 13; i++) getchar();
        scanf("%d", &bx);
        // ", Y+"
        for (int i = 0; i < 4; i++) getchar();
        scanf("%d", &by);

        // "\nPrize: X="
        for (int i = 0; i < 10; i++) getchar();
        scanf("%d", &px);
        // ", Y="
        for (int i = 0; i < 4; i++) getchar();
        scanf("%d", &py);
        getchar();

        answer += minimum_tokens(ax, ay, bx, by, px + 1e13, py + 1e13);
    } while (scanf("%c", &c) != EOF);

    cout << answer << endl;
}
