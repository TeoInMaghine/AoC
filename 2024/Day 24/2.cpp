#include <bits/stdc++.h>
using namespace std;

enum Op { AND, OR, XOR };

// id: value, subscribers (ids of the operations)
map<string, pair<bool,vector<int>>> wires;

struct Gate {
    Op op;
    string operand1, operand2, result;
    bool calculated1, calculated2;
    bool calculated;

    void calculate() {
        bool res;

        bool op1 = wires[operand1].first, op2 = wires[operand2].first;
        switch (op) {
            case AND:
                res = op1 & op2;
                break;
            case OR:
                res = op1 | op2;
                break;
            case XOR:
                res = op1 ^ op2;
                break;
        }

        wires[result].first = res;
        calculated = true;
    }
};
vector<Gate> gates;

deque<string> unprocessed;

int main() {
    deque<string> original_wires;
    string s;
    while (getline(cin, s)) {
        if (s.size() == 0) break;

        string wire = s.substr(0,3);
        wires[wire].first = s[5] == '1';
        unprocessed.push_back(wire);
        original_wires.push_back(wire);
    }

    int id = 0;
    while (getline(cin, s)) {
        int second_space_i = s.find(' ', 4);

        Gate gate;
        gate.op = s[4] == 'A' ? AND : s[4] == 'O' ? OR : XOR;
        gate.operand1 = s.substr(0,3);
        gate.operand2 = s.substr(second_space_i+1,3);
        gate.result = s.substr(second_space_i+8,3);
        gate.calculated1 = false;
        gate.calculated2 = false;
        gate.calculated = false;
        gates.push_back(gate);

        wires[gate.operand1].second.push_back(id);
        wires[gate.operand2].second.push_back(id);
        id++;
    }

    wires["x00"].first = true;
    for (int i = 0; i < 44; i++) {
        wires["y00"].first = true;
        for (int j = 0; j < 44; j++) {
            // reset unprocessed
            unprocessed = original_wires;

            // reset gates
            for (auto it = gates.begin(); it != gates.end(); ++it) {
                it->calculated1 = false;
                it->calculated2 = false;
                it->calculated = false;
            }

            while (!unprocessed.empty()) {
                string curr = unprocessed.front(); unprocessed.pop_front();
                for (const auto& sub_id : wires[curr].second) {
                    Gate *gate = &gates[sub_id];

                    if (gate->operand1 == curr) gate->calculated1 = true;
                    if (gate->operand2 == curr) gate->calculated2 = true;

                    if (!gate->calculated && gate->calculated1 && gate->calculated2) {
                        gate->calculate();
                        unprocessed.push_back(gate->result);
                    }
                }
            }

            long answer = 0;
            long bit_mult = 1;
            for (auto it = wires.lower_bound("z00"); it != wires.end(); ++it) {
                bool value = it->second.first;

                // this weird-a** process is to start by the LSB instead of the MSB
                answer += value * bit_mult;
                bit_mult <<= 1;
            }

            long long expected = ((long)1<<i) + ((long)1<<j);
            if (answer != expected) {
                cout << answer << ", expected: " << expected << '\n';
                cout << i << ' ' << j << '\n';
            }

            wires[format("y{:02}", j)].first = false;
            wires[format("y{:02}", j+1)].first = true;
        }
        wires["y44"].first = false;

        wires[format("x{:02}", i)].first = false;
        wires[format("x{:02}", i+1)].first = true;

        cout << "(remember that I already switched a few gates)" << '\n';
    }
}
