#include <bits/stdc++.h>
using namespace std;

int main() {
    long unsigned A = 190384113204239;

    while (A != 0) {
        cout << (((((A & 7) ^ 2) ^ (A >> ((A & 7) ^ 2))) ^ 7) & 7) << ',';
        A >>= 3;
    }
}

