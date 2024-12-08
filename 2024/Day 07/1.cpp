#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll result;
deque<ll> nums;

int solve() {
    ll x = nums.front();
    nums.pop_front();
    
    for (int i = 0; i < pow(2,nums.size()); i++) {
        ll res = x;
        bitset<32> permutation(i);
        for (int j = 0; j < nums.size(); j++) {
            if (permutation.test(j)) {
                res += nums[j];
            } else {
                res *= nums[j];
            }
        }

        if (res == result) {
            cout << result << endl;
            return result;
        }
    }

    return 0;
}

int main() {
    char c;
    ll x = 0;
    ll answer = 0;
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
