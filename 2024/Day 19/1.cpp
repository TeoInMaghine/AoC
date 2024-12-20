#include <bits/stdc++.h>
using namespace std;

map<int,bool> memo;
set<string> towels;
string line;

bool solve(int start) {
    if (start >= line.size()) return true;

    if (memo.contains(start)) return memo[start];

    bool solvable = false;
    for (int count = 1; count < line.size() - start + 1; count++) {
        string sub = line.substr(start, count);
        if (towels.contains(sub) && solve(start + count)) {
            solvable = true;
            break;
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

    int answer = 0;
    while (getline(cin, line)) {
        answer += solve(0);
        memo.clear();
    }

    cout << answer << '\n';
}
