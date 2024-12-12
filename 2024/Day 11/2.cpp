#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

// value, blinks: # stones
map<pair<ll,int>, ll> memo;

ll count_stones(ll value, int blinks) {
    if (blinks <= 0) {
        return 1;
    }

    blinks--;
    ll stones_count = 0;

    pair<ll,int> key = {value, blinks+1};
    if (memo.contains(key)) {
        return memo[key];
    }

    if (value == 0) {
        stones_count = count_stones(1, blinks);
    } else {
        int digits = (int) log10 (value) + 1;
        if (digits % 2 == 0) {
            digits /= 2;
            ll left = value / (ll) pow(10, digits);
            ll right = value % (ll) pow(10, digits);
            stones_count = count_stones(left, blinks) + count_stones(right, blinks);
        } else {
            stones_count = count_stones(value * 2024, blinks);
        }
    }

    memo[key] = stones_count;
    return stones_count;
}

int main() {
    string line;
    getline(cin, line);
    istringstream this_line(line);
    istream_iterator<int> begin(this_line), end;
    vector<int> nums(begin, end);

    ll answer = 0;
    for (int num : nums) {
        answer += count_stones(num, 25);
    }

    cout << answer << endl;
}

