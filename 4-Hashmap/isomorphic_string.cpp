#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, int> sCount;    
        unordered_map<char, int> tCount;    
        int length = s.size(); // size of 's' is equal to 't'
        // initialize
        for(int i = 0; i < length; i++) {
            sCount[s[i]] = 0;
        }
        for(int i = 0; i < length; i++) {
            tCount[t[i]] = 0;
        }
        // counting
        for(int i = 0; i < length; i++) {
            
        }
    }
};

int main() {
    Solution sol;
    string s = "egg";
    string t = "add";
    cout << sol.isIsomorphic(s, t);
}
