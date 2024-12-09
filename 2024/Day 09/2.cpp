#include <bits/stdc++.h>
using namespace std;

// position: size
map< int, int > frees;
// position: <size,id>
map< int, pair<int,int> > files, moved_files;

int main() {

    char c;
    int id = 0;
    bool is_file = true;
    int position = 0;
    while (scanf("%c", &c) != EOF) {
        if (c == '\n') break;
        int size = c - '0';

        if (size != 0) {
            if (is_file) {
                files[position] = {size,id};
            } else {
                frees[position] = size;
            }
        }

        id += is_file;
        is_file = !is_file;
        position += size;
    }

    // iterate from rightmost file
    for (auto it = files.rbegin(); it != files.rend(); ) {
        int pos = it->first;
        auto[size, id] = it->second;

        // iterate through leftmost free blocks up until the files' position
        auto jt = frees.begin();
        for ( ; jt != frees.end() && jt->first < pos; ++jt)
            if (jt->second >= size)
                break;

        auto[free_pos, free_size] = *jt;

        // check that there is a free block that fits, and that it's before the file
        if (jt != frees.end() && free_pos < pos) {
            // remove occuppied free space
            frees.erase(free_pos);

            // create new free block if necessary
            int remaining_free_size = free_size - size;
            if (remaining_free_size > 0) {
                frees[free_pos + size] = remaining_free_size;
            }

            // add new free space in the previous place of the file
            frees[pos] = size;

            // add file to moved_files
            moved_files[free_pos] = {size, id};
            // remove file from files
            it = decltype(it)( files.erase(next(it).base()) );
        } else {
            ++it;
        }
    }

    long long answer = 0;
    for (auto& [pos, value] : files) {
        auto [size,id] = value;
        
        for (int i = 0; i < size; i++)
            answer += (pos + i) * id;
    }

    for (auto& [pos, value] : moved_files) {
        auto [size,id] = value;
        
        for (int i = 0; i < size; i++)
            answer += (pos + i) * id;
    }

    cout << answer << endl;
}
