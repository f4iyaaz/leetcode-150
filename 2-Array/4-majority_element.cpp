#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        double threshold = floor(nums.size() / 2.0);
        int majority_count = 0;
        map<int, int> m;
        for(int i = 0; i < nums.size(); i++) {
            m[nums[i]] = 0;
        }
        for(int i = 0; i < nums.size(); i++) {
            m[nums[i]]++;
        }
        for(auto i = m.begin(); i != m.end(); i++) {
            if(i->second > threshold) {
                return i->first;
            }
        }
        return -1;
    }
};

int main() {
    vector<int> v = {3,2,3};
    Solution soln;
    cout << soln.majorityElement(v);
}