#include <bits/stdc++.h>
using namespace std;

map<int, set<int>> relations;

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

    int corrects = 0;
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

        bool followsRules = true;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            for (int j = i+1; j < nums.size(); j++) {
                if (relations[nums[j]].contains(num)) {
                    followsRules = false;
                }
            }
        }

        corrects += followsRules;
        if (followsRules)
            total += nums[nums.size() / 2];
    }

    cout << corrects << endl;
    cout << total << endl;

}
