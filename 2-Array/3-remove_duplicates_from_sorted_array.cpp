#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        int curr = nums[k];
        for(int i = 1; i < nums.size();) {
            
            if(curr == nums[i]) {
                nums.erase(nums.begin()+(i));
                // cout << nums[i];
            }else{
                k++;
                i++;
                curr = nums[k];
            }
            // cout << nums[i];
        }
        cout << "\n";
        return nums.size();
    }
};

int main() {
    vector<int> v = {0,0,1,1,1,2,2,3,3,4};
    Solution soln;
    cout << soln.removeDuplicates(v);
}