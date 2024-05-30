#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {


    int low = 0;
    int high = nums.size() - 1;
    int mid = (low + high) / 2;
    int target_data = target;
    bool flag = 0;
    // cout << mid;

    while(low <= high) {
        if(nums[mid] == target_data) {
            return mid;
            // break;
        }
        else if(nums[mid] > target_data) {
            high = mid - 1;
            mid = (low + high) / 2;
        }
        else if(nums[mid] < target_data) {
            low = mid + 1;
            mid = (low + high) / 2;
        }
    }
    return low;
    }
};

int main() {
    vector<int> data = {9, 0, 3, 2, 1, 4, 8, 5, 6, 7}; // 0 1 2 3 4 5 6 7 8 9
    int target = 5;
    Solution soln;
    soln.searchInsert(data, target);
}