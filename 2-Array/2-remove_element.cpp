#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        nums.erase(remove(nums.begin(), nums.end(), val), nums.end()); // idiom
        return nums.size();
    }
};
 
int main() {
    vector<int> v = {0,1,2,2,3,0,4,2};
    int val = 2;

    Solution soln;
    cout << soln.removeElement(v, val);
}