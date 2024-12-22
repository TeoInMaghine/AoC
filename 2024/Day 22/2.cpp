#include <bits/stdc++.h>
using namespace std;

const int PRUNE = 16777216;

int main() {
    // change sequence: sum of the prices for that sequence for all monkeys
    int sum_prices[19][19][19][19] = {0};

    string line;
    while (getline(cin, line)) {
        // wether the change-sequence was already found for this monkey
        bool found[19][19][19][19] = {false};
        int changes[4];

        long secret = stoi(line);
        int prev_price = secret % 10;

        for (int i = 0; i < 2000; i++) {
            secret = ((secret << 6) ^ secret) % PRUNE;
            secret = ((secret >> 5) ^ secret) % PRUNE;
            secret = ((secret << 11) ^ secret) % PRUNE;

            const int price = secret % 10;
            changes[i % 4] = price - prev_price;

            if (i >= 3) {
                const int i1 = changes[i % 4] + 9;
                const int i2 = changes[(i+1) % 4] + 9;
                const int i3 = changes[(i+2) % 4] + 9;
                const int i4 = changes[(i+3) % 4] + 9;
                if (!found[i1][i2][i3][i4]) {
                    found[i1][i2][i3][i4] = true;
                    sum_prices[i1][i2][i3][i4] += price;
                }
            }

            prev_price = price;
        }
    }

    int answer = 0;
    for (int i = 0; i < 19; i++)
        for (int j = 0; j < 19; j++)
            for (int k = 0; k < 19; k++)
                for (int w = 0; w < 19; w++)
                    answer = max(answer, sum_prices[i][j][k][w]);

    cout << answer << '\n';
}
