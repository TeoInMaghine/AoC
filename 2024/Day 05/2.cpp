#include <bits/stdc++.h>
using namespace std;

map<int, set<int>> relations;

bool comp(int a, int b) {
    return relations[a].contains(b);
}

int main() {
    for (int i = 0; i < 1176; i++) {
        char c;
        int a, b;
        scanf("%d", &a);
        scanf("%c", &c);
        scanf("%d", &b);
        scanf("%c", &c);

        relations[a].insert(b);
    }

    int total = 0;

    string tmp;
    getline(cin, tmp);
    for (int i = 0; i < 185; i++) {
        getline(cin, tmp);
        vector<int> nums;
        stringstream ss(tmp);
        int num;
        while(ss >> num)
            nums.push_back(num);

        if (!is_sorted(nums.begin(), nums.end(), comp)) {
            sort(nums.begin(), nums.end(), comp);
            total += nums[nums.size() / 2];
        }
    }

    cout << total << endl;
}
