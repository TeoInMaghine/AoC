#include <bits/stdc++.h>
using namespace std;

const int PRUNE = 16777216;

int main() {
    // change sequence: sum of the prices for that sequence for all monkeys
    map<tuple<int,int,int,int>,int> sum_prices;

    string line;
    while (getline(cin, line)) {
        // wether the change-sequence was already found for this monkey
        set<tuple<int,int,int,int>> found;
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
                tuple<int,int,int,int> change_sequence = { changes[i % 4], changes[(i+1) % 4], changes[(i+2) % 4], changes[(i+3) % 4] };
                if (!found.contains(change_sequence)) {
                    found.insert(change_sequence);
                    sum_prices[change_sequence] += price;
                }
            }

            prev_price = price;
        }
    }

    int answer = 0;
    for (const auto& [change_sequence,sum_price] : sum_prices) {
        answer = max(answer, sum_price);
    }
    cout << answer << '\n';
}
