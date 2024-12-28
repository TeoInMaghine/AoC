#include <bits/stdc++.h>
using namespace std;

const int V = 26 * 26;
const int n = 3;

// PC: connections
set<int> adj[V];
deque<int> unvisited;
set<int> largest_interconnected;

string id_to_pc(int id) {
    string s = "  ";
    s[0] = id / 26 + 'a';
    s[1] = id % 26 + 'a';
    return s;
}

int main() {
    string s;
    while (getline(cin,s)) {
        int pc1 = 26 * (s[0] - 'a') + s[1] - 'a';
        int pc2 = 26 * (s[3] - 'a') + s[4] - 'a';
        adj[pc1].insert(pc2);
        adj[pc2].insert(pc1);
    }

    for (int v = 0; v < V; v++) {
        if (!adj[v].empty()) unvisited.push_back(v);
    }

    while (!unvisited.empty()) {
        int curr = unvisited.front(); unvisited.pop_front();

        set<int> interconnected;
        for (int next : adj[curr]) {
            bool connected = true;
            for (int inter : interconnected) {
                if (!adj[next].contains(inter)) {
                    connected = false;
                    break;
                }
            }

            if (connected) {
                interconnected.insert(next);
            }
        }
        interconnected.insert(curr);

        if (interconnected.size() > largest_interconnected.size())
            largest_interconnected = interconnected;
    }

    cout << largest_interconnected.size() << '\n';
    for (int inter : largest_interconnected) {
        cout << id_to_pc(inter) << ',';
    }
    cout << '\n';
}
