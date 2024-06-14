#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;
        if(nums[low] < nums[high]) {
            return nums[low];
        }

        while(low < high) {
            int mid = (low + high) / 2;
            if(nums[mid] > nums[high]) {
                low = mid + 1;
            }
            else {
                high = mid;
            }
        }
        return nums[low];
    }
};

int main() {
    vector<int> v = {4,5,6,7,0,1,2};
    Solution sol;
    cout << sol.findMin(v);
}