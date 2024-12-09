#include <bits/stdc++.h>
using namespace std;

int main() {
    // -1 means free
    vector<int> disk;
    char c;
    int id = 0;
    bool file = true;
    while (scanf("%c", &c) != EOF) {
        if (c == '\n') break;
        int x = c - '0';

        for (int i = 0; i < x; i++) {
            disk.push_back(file ? id : -1);
        }

        id += file;
        file = !file;
    }

    int n = disk.size();

    int j = n - 1;
    for (int i = 0; i < j; ) {
        if (disk[i] == -1) {
            if (disk[j] != -1)
                iter_swap(disk.begin() + i, disk.begin() + j);
            else
                j--;
        } else {
            i++;
        }
    }

    long long answer = 0;
    for (int i = 0; i < n; i++) {
        if (disk[i] == -1) continue;

        answer += i * disk[i];
    }

    cout << answer << endl;
}
