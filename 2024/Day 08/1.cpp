#include <bits/stdc++.h>
using namespace std;

vector<string> grid;
multimap<char, pair<int,int>> antennas;

inline bool is_in_grid(int i, int j) {
    return i >= 0 && i < grid.size() && j >= 0 && j < grid[0].size();
}

int main() {
    string s;
    int i = 0;
    while (getline(cin, s)) {
        grid.push_back(s);
        for (int j = 0; j < s.size(); j++) {
            if (s[j] != '.') antennas.insert({s[j], {i, j}});
        }
        i++;
    }
    
    auto it = antennas.begin();
    while (it != antennas.end()) {
        int it_i = it->second.first;
        int it_j = it->second.second;

        char key = it->first;
        auto jt = it;
        for (++jt; jt->first == key; ++jt) {
            int jt_i = jt->second.first;
            int jt_j = jt->second.second;

            // deltas from it to jt
            int di = jt_i - it_i;
            int dj = jt_j - it_j;

            // an is short for antinode
            for (int an_i = jt_i, an_j = jt_j; is_in_grid(an_i, an_j); an_i += di, an_j += dj)
                grid[an_i][an_j] = '#';

            for (int an_i = it_i, an_j = it_j; is_in_grid(an_i, an_j); an_i -= di, an_j -= dj)
                grid[an_i][an_j] = '#';
        }

        ++it;
    }

    int answer = 0;
    for (auto& s : grid)
        answer += count(s.begin(), s.end(), '#');
    cout << answer << endl;
}
