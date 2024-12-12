#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long

int count_stones(ll value, int blinks) {
    if (blinks <= 0) {
        return 1;
    }

    blinks--;

    if (value == 0) {
        return count_stones(1, blinks);
    }

    int digits = (int) log10 (value) + 1;
    if (digits % 2 == 0) {
        digits /= 2;
        ll left = value / (ll) pow(10, digits);
        ll right = value % (ll) pow(10, digits);
        return count_stones(left, blinks) + count_stones(right, blinks);
    }
    
    return count_stones(value * 2024, blinks);
}

int main() {
    string line;
    getline(cin, line);
    istringstream this_line(line);
    istream_iterator<int> begin(this_line), end;
    vector<int> nums(begin, end);

    int answer = 0;
    for (int num : nums) {
        answer += count_stones(num, 25);
    }

    cout << answer << endl;
}
