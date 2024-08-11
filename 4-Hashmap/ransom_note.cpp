#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, char> m;

    m[1] = '1';
    m[2] = '2';
    m[3] = '3';

    for(auto i = m.begin(); i != m.end(); i++) {
        cout << i->first << ": " << i->second << endl;
    }

    string s = "aaa";
    for(int i = 0; i < s.size(); i++) {
        cout << s[i] << endl;
    }
}