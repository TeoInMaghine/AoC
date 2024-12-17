#include <bits/stdc++.h>
using namespace std;

long unsigned A = 0;

int main() {
    // I want it to print:
    int goals[16] = {2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0};
    reverse(goals, goals + 16);

    for (int goal : goals) {
        A <<= 3;

        int next_bits = 8;
        // from bigger to smaller to get the smallest possible "next_bits"
        for (int i = 7; i >= 0; i--) {
            long unsigned possible_A = A + i;
            int out = ((((possible_A & 7) ^ 2) ^ (possible_A >> ((possible_A & 7) ^ 2))) ^ 7) & 7;
            if (out == goal) next_bits = i;
        }

        A += next_bits;
    }

    cout << A << endl;
}
