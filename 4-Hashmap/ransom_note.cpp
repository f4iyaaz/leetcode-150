#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> wordCount1;
        unordered_map<char, int> wordCount2;
        // initialize the character count
        for(int i = 0; i < ransomNote.size(); i++) {
            wordCount1[ransomNote[i]] = 0;
        }
        for(int i = 0; i < magazine.size(); i++) {
            wordCount2[magazine[i]] = 0;
        }
        // counting the characters
        for(int i = 0; i < ransomNote.size(); i++) {
            wordCount1[ransomNote[i]] = wordCount1[ransomNote[i]] + 1;
        }
        for(int i = 0; i < magazine.size(); i++) {
            wordCount2[magazine[i]] = wordCount2[magazine[i]] + 1;
        }
        // check 
        for(int i = 0; i < ransomNote.size(); i++) {
            if(!wordCount2.count(ransomNote[i])) {
                return false;
            }
            else {
                if(wordCount1[ransomNote[i]] <= wordCount2[ransomNote[i]]) {
                    continue;
                }
                else {
                    return false;
                }
            }
        }
        return true;
    }
};

int main() {

    string s = "aa";
    string c = "aab";

    Solution sol;
    // sol.canConstruct(s, c);
    cout << sol.canConstruct(s, c) << endl;
}
