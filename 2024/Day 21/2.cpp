#include <bits/stdc++.h>
using namespace std;

#define ll long long

const pair<int,int> NUM_POSITIONS[10] = { {3,1}, {2,0}, {2,1}, {2,2}, {1,0}, {1,1}, {1,2}, {0,0}, {0,1}, {0,2} };
const pair<int,int> NUM_A_POS = {3,2};
const int NUM_GAP_I = 3;
const int NUM_GAP_J = 0;

const pair<int,int> DIR_U_POS = {0,1};
const pair<int,int> DIR_L_POS = {1,0};
const pair<int,int> DIR_D_POS = {1,1};
const pair<int,int> DIR_R_POS = {1,2};
const pair<int,int> DIR_A_POS = {0,2};
const int DIR_GAP_I = 0;
const int DIR_GAP_J = 0;


deque<pair<int,int>> add_next_goals_numeral(deque<pair<int,int>> goals, pair<int,int> curr) {
    deque<pair<int,int>> next_goals;
    for (const auto& goal : goals) {
        const auto& [i,j] = curr;
        const auto& [ni,nj] = goal;
        const int di = ni - i, dj = nj - j;

        // treat separately in cases where the gap needs to be avoided
        if(ni == NUM_GAP_I && j == NUM_GAP_J) { // from top-left to bottom-right
            // right
            for (int c = 0; c < dj; c++) next_goals.push_back(DIR_R_POS);
            // down
            for (int c = 0; c < di; c++) next_goals.push_back(DIR_D_POS);
        }
        else if(i == NUM_GAP_I && nj == NUM_GAP_J) { // from bottom-right to top-left
            // up
            for (int c = 0; c < -di; c++) next_goals.push_back(DIR_U_POS);
            // left
            for (int c = 0; c < -dj; c++) next_goals.push_back(DIR_L_POS);
        }
        else { // otherwise, prioritize to minimize moves

            // go to the ones farthest away from A first
            for (int c = 0; c < -dj; c++) next_goals.push_back(DIR_L_POS);
            for (int c = 0; c < di; c++) next_goals.push_back(DIR_D_POS);

            // then the ones closest to A
            // also, prioritize up rather then right, not sure why actually,
            // but I'm guessing it affects moves down the line
            for (int c = 0; c < -di; c++) next_goals.push_back(DIR_U_POS);
            for (int c = 0; c < dj; c++) next_goals.push_back(DIR_R_POS);
        }

        next_goals.push_back(DIR_A_POS);
        curr = goal;
    }

    return next_goals;
}

// curr, goal, keypads: steps
map<tuple<int,int, int,int, int>, ll> memo;
ll count_minimum_steps(pair<int,int> curr, pair<int,int> goal, int keypads) {

    const auto& [i,j] = curr;
    const auto& [ni,nj] = goal;

    const int di = ni - i, dj = nj - j;
    if (keypads == 1) return abs(di) + abs(dj) + 1;

    const tuple<int,int, int,int, int>& key = {i,j,ni,nj,keypads};
    if (memo.contains(key)) return memo[key];

    deque<pair<int,int>> next_goals;
    // treat separately in cases where the gap needs to be avoided
    if(i == DIR_GAP_I && nj == DIR_GAP_J) { // from top-right to bottom-left
        // down
        for (int c = 0; c < di; c++) next_goals.push_back(DIR_D_POS);
        // left
        for (int c = 0; c < -dj; c++) next_goals.push_back(DIR_L_POS);
    }
    else if(ni == DIR_GAP_I && j == DIR_GAP_J) { // from bottom-left to top-right

        // right
        for (int c = 0; c < dj; c++) next_goals.push_back(DIR_R_POS);
        // up
        for (int c = 0; c < -di; c++) next_goals.push_back(DIR_U_POS);
    }
    else { // otherwise, prioritize to minimize moves

        // go to the ones farthest away from A first
        for (int c = 0; c < -dj; c++) next_goals.push_back(DIR_L_POS);
        for (int c = 0; c < di; c++) next_goals.push_back(DIR_D_POS);

        // then the ones closest to A
        // also, prioritize up rather then right, not sure why actually,
        // but I'm guessing it affects moves down the line
        for (int c = 0; c < -di; c++) next_goals.push_back(DIR_U_POS);
        for (int c = 0; c < dj; c++) next_goals.push_back(DIR_R_POS);
    }

    next_goals.push_back(DIR_A_POS);

    ll steps = 0;
    // prev starts in A always, 'cause for the previous direction at the end
    // the A button is always pressed
    pair<int,int> prev = DIR_A_POS;
    for (const auto& next_goal : next_goals) {
        steps += count_minimum_steps(prev, next_goal, keypads-1);
        prev = next_goal;
    }

    memo[key] = steps;
    return steps;
}

int main() {
    string line;
    ll answer = 0;
    while (getline(cin, line)) {
        deque<pair<int,int>> goals;

        for (char c : line)
            goals.push_back((c == 'A') ? NUM_A_POS : NUM_POSITIONS[c - '0']);

        deque<pair<int,int>> next_goals = add_next_goals_numeral(goals, NUM_A_POS);

        ll steps = 0;
        pair<int,int> prev = DIR_A_POS;
        for (const auto& goal : next_goals) {
            steps += count_minimum_steps(prev, goal, 25);
            prev = goal;
        }

        answer += steps * stoi(line.substr(0, 3));
    }

    cout << answer << '\n';
}
