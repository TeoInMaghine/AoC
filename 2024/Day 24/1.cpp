#include <bits/stdc++.h>
using namespace std;

enum Op { AND, OR, XOR };

// id: value, subscribers (ids of the operations)
map<string, pair<bool,vector<int>>> wires;

struct Operation {
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
vector<Operation> operations;

deque<string> unprocessed;

int main() {
    string s;
    while (getline(cin, s)) {
        if (s.size() == 0) break;

        string wire = s.substr(0,3);
        wires[wire].first = s[5] == '1';
        unprocessed.push_back(wire);
    }

    int id = 0;
    while (getline(cin, s)) {
        int second_space_i = s.find(' ', 4);

        Operation op;
        op.op = s[4] == 'A' ? AND : s[4] == 'O' ? OR : XOR;
        op.operand1 = s.substr(0,3);
        op.operand2 = s.substr(second_space_i+1,3);
        op.result = s.substr(second_space_i+8,3);
        op.calculated1 = false;
        op.calculated2 = false;
        op.calculated = false;
        operations.push_back(op);

        wires[op.operand1].second.push_back(id);
        wires[op.operand2].second.push_back(id);
        id++;
    }

    while (!unprocessed.empty()) {
        string curr = unprocessed.front(); unprocessed.pop_front();
        for (const auto& sub_id : wires[curr].second) {
            Operation *op = &operations[sub_id];

            if (op->operand1 == curr) op->calculated1 = true;
            if (op->operand2 == curr) op->calculated2 = true;

            if (!op->calculated && op->calculated1 && op->calculated2) {
                op->calculate();
                unprocessed.push_back(op->result);
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
    cout << answer << '\n';
}
