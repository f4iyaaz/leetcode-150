#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    // bool check(unordered_map<char, char> &st, unordered_map<char, char> ts) {
    //     return true;
    // }
    // s can't map more than one characters of t
    // t can't map more than one characters of s
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> s_to_t;
        unordered_map<char, char> t_to_s;
        for(int i = 0; i < s.size(); i++) {
            if(s_to_t.empty()) {
                s_to_t[s[i]] = t[i];
                t_to_s[t[i]] = s[i];
            }
            else {
                if(s_to_t.count(s[i]) || t_to_s.count(t[i])) {
                    if(s_to_t[s[i]] != t[i]) {
                        return false;
                    }
                    if(t_to_s[t[i]] != s[i]) {
                        return false;
                    }
                }
                else {
                    s_to_t[s[i]] = t[i];
                    t_to_s[t[i]] = s[i];
                }
            }
        }
        return true;
    }
};

int main() {
    Solution sol;
    string s = "bbbaaaba";
    string t = "aaabbbba";
    // string s = "egg";
    // string t = "add";
    // string s = "badc";
    // string t = "baba";
    cout << sol.isIsomorphic(s, t);
}
