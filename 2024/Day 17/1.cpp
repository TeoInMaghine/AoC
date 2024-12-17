#include <bits/stdc++.h>
using namespace std;

int A, B, C;
// inst, operand
vector<pair<int,int>> program;

int main() {

    char c[13];
    // "Register A: "
    scanf("%12c", c);
    scanf("%d", &A);

    // "\nRegister B: "
    scanf("%13c", c);
    scanf("%d", &B);

    // "\nRegister C: "
    scanf("%13c", c);
    scanf("%d", &C);

    // "\n\nProgram:"
    scanf("%10c", c);

    while (scanf("%c", c) != EOF) {
        int inst, operand;
        scanf("%d", &inst);
        // ","
        scanf("%c", c);
        scanf("%d", &operand);

        program.push_back({inst, operand});
    }

    // pc: program counter
    for (int pc = 0; pc < program.size(); ) {
        const auto [inst, literal] = program[pc];
        const int combo = literal == 4 ? A :
                          literal == 5 ? B :
                          literal == 6 ? C :
                          literal;

        switch (inst) {
            // adv
            case 0:
                // divide A by 2^combo
                A >>= combo;
                break;
            // bxl
            case 1:
                // bitwise XOR of B with literal
                B ^= literal;
                break;
            // bst
            case 2:
                // set B to combo % 8
                B = combo & 7;
                break;
            // jnz
            case 3:
                if (A != 0) {
                    // this seems to only happen at the end and go to 0,
                    // so I won't worry for cases where the literal is not
                    // 0 and should be divided by 2 or something like that

                    // jump to the literal-th instruction
                    pc = literal;
                    continue; // to avoid pc++
                }
                break;
            // bxc
            case 4:
                // bitwise XOR of B with C
                B ^= C;
                break;
            // out
            case 5:
                // print combo % 8
                cout << (combo & 7) << ',';
                break;
            // bdv
            case 6:
                // divide A by 2^combo, but store in B
                B = A >> combo;
                break;
            // cdv
            default:
                // divide A by 2^combo, but store in C
                C = A >> combo;
                break;
        }
        pc++;
    }
}
