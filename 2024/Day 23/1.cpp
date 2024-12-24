#include <bits/stdc++.h>
using namespace std;

#define PC pair<char,char>

// PC: PC
map<PC, set<PC>> connections;

int main() {
    string s;
    while (getline(cin,s)) {
        PC pc1, pc2;
        pc1 = { s[0], s[1] };
        pc2 = { s[3], s[4] };
        connections[pc1].insert(pc2);
        connections[pc2].insert(pc1);
    }
}
