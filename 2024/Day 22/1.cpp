#include <bits/stdc++.h>
using namespace std;

#define ll long long
const ll PRUNE = 16777216;

int main() {
    ll answer = 0;
    string line;
    while (getline(cin, line)) {
        ll secret = stoi(line);
        for (int i = 0; i < 2000; i++) {
            secret = ((secret << 6) ^ secret) % PRUNE;
            secret = ((secret >> 5) ^ secret) % PRUNE;
            secret = ((secret << 11) ^ secret) % PRUNE;
        }
        answer += secret;
    }

    cout << answer << '\n';
}
