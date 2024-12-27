#include <bits/stdc++.h>
using namespace std;

const int V = 26 * 26;
const int n = 3;

// PC: connections
set<int> adj[V];
bool visited[V] = { false };

void DFS(int n, int v, int start, int& count) {
    visited[v] = true;

    // path of length (n-1) found
    if (n == 0) {
        // unmark to make it usable again
        visited[v] = false;
        count += adj[v].contains(start);
        return;
    }

    // search every possible path of length (n-1)
    for (const auto& next : adj[v])
        if (!visited[next])
            DFS(n - 1, next, start, count);

    // unmark to make it usable again
    visited[v] = false;
}

int main() {
    string s;
    while (getline(cin,s)) {
        int pc1 = 26 * (s[0] - 'a') + s[1] - 'a';
        int pc2 = 26 * (s[3] - 'a') + s[4] - 'a';
        adj[pc1].insert(pc2);
        adj[pc2].insert(pc1);
    }

    int count = 0;

    // check PCs starting with 't'
    const int from = ('t' - 'a') * 26, end = ('t' - 'a' + 1) * 26;
    for (int v = from; v < end; v++) {
        if (adj[v].empty()) continue;

        DFS(n - 1, v, v, count);
        visited[v] = true;
    }
    count /= 2;

    cout << count << '\n';
}
