#include <bits/stdc++.h>
using namespace std;
#define ll unsigned long long

ll result;
vector<ll> nums;

ll concatenate(ll left, ll right) {
    int r_digits = (int) log10 (right) + 1;
    return left * (ll) pow(10,r_digits) + right;
}

ll solve() {
    for (int i = 0; i < pow(3,nums.size()-1); i++) {
        ll res = nums[0];
        ll number = i;
        for (int j = 0; j < nums.size()-1; j++) {
            ll digit = number % 3;
            if (digit == 0) {
                res += nums[j+1];
            } else if (digit == 1) {
                res *= nums[j+1];
            } else {
                res = concatenate(res, nums[j+1]);
            }
            number /= 3;
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
