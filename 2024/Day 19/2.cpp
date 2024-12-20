#include <bits/stdc++.h>
using namespace std;

map<int,long> memo;
set<string> towels;
string line;

long solve(int start) {
    if (start >= line.size()) return 1;

    if (memo.contains(start)) return memo[start];

    long solvable = 0;
    for (int count = 1; count < line.size() - start + 1; count++) {
        string sub = line.substr(start, count);
        if (towels.contains(sub)) {
            solvable += solve(start + count);
        }
    }

    memo[start] = solvable;
    return solvable;
}


int main() {
    getline(cin, line);

    size_t pos = 0;
    string towel;
    while ((pos = line.find(", ")) != string::npos) {
        towel = line.substr(0, pos);
        towels.insert(towel);
        line.erase(0, pos + 2);
    }
    towels.insert(towel);

    // Ignore \n
    getchar();

    long answer = 0;
    while (getline(cin, line)) {
        answer += solve(0);
        memo.clear();
    }

    cout << answer << '\n';
}
