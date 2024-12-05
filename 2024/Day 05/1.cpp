#include <bits/stdc++.h>
using namespace std;

const int not_set = 1000;

multimap<int, int> relations;
int values[100];
multimap<int, int> order;

int main() {
    // 1000 es un valor al que seguro no llego
    fill(values, values + 100, not_set);

    for (int i = 0; i < 21; i++) {
        char c;
        int a, b;
        scanf("%d", &a);
        scanf("%c", &c);
        scanf("%d", &b);
        scanf("%c", &c);

        relations.insert({a, b});
    }

    while (not relations.empty()) {
        int first_num = relations.begin()->first;

        int min = not_set;
        for (auto[it, end] = relations.equal_range(first_num); it != end; ++it)
            if (values[it->second] != not_set)
                min = std::min(min, values[it->second]);

        if (min == not_set) {
            if (values[first_num] == not_set) {
                values[first_num] = 0;
                order.insert({ values[first_num], first_num });
            }
        } else {
            if (values[first_num] == not_set) {
                values[first_num] = min - 1;
                order.insert({ values[first_num], first_num });
            }

            vector<pair<int, int>> ops;
            for (auto it = order.lower_bound(values[first_num]); it != order.end(); ) {
                int num = it->second;
                if (num != first_num) {
                    values[num] += 1;
                    ops.push_back(*it);
                    it = order.erase(it);
                } else {
                    ++it;
                }
            }

            for (auto it = ops.begin(); it != ops.end(); ++it)
                order.insert(*it);
        }

        for (auto[it, end] = relations.equal_range(first_num); it != end; ++it) {
            int num = it->second;
            if (values[num] == not_set) {
                values[num] = values[first_num] + 1;
                order.insert({ values[num], num });
            }
        }

        relations.erase(first_num);
    }

    // string tmp;
    // getline(cin, tmp);
    // for (int i = 0; i < 6; i++) {
    //     getline(cin, tmp);
    //     vector<int> nums;
    //     stringstream ss(tmp);
    //     int num;
    //     while(ss >> num)
    //         nums.push_back(num);
    //
    //     // I don't care for now
    // }
    //
    // cout << 0 << endl;

    for (int i = 0; i < 100; i++)
        if (values[i] != not_set)
            cout << i << ": " << values[i] << endl;

}
