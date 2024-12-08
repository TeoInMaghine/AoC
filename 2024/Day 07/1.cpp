#include <bits/stdc++.h>
using namespace std;
#define ll unsigned long long

ll result;
vector<ll> nums;

ll solve() {
    for (int i = 0; i < pow(2,nums.size()-1); i++) {
        ll res = nums[0];
        bitset<32> permutation(i);
        for (int j = 0; j < nums.size()-1; j++) {
            if (permutation.test(j)) {
                res += nums[j+1];
            } else {
                res *= nums[j+1];
            }
        }

        if (res == result) {
            return result;
        }
    }

    return 0;
}

int main() {
    char c;
    ll x = 0;
    uint64_t answer = 0;
    while (scanf("%c", &c) != EOF) {
        if (isdigit(c)) {
            x = x * 10 + (c - '0');
        } else {
            if (c == ':') {
                result = x;
                scanf("%c", &c);
            } else if (c != '\n') {
                nums.push_back(x);
            } else {
                nums.push_back(x);
                answer += solve();
                nums.clear();
            }

            x = 0;
        }
    }

    cout << answer << endl;
}
