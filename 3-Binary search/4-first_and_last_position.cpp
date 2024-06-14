#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
        int low = 0;
        int high = nums.size() - 1;
        int mid = 0;
        int index = -1;
        vector<int> v;

        if(nums.size() == 0) {
            return v = {-1, -1};
        }

        while(low <= high) {
            mid = (low + high) / 2;
            if(target == nums[mid]) {
                index = mid;
                break;
            }
            else if(target < nums[mid]) {
                high = mid - 1;
            }
            else if(target > nums[mid]) {
                low = mid + 1;
            }
        }


        if(index == 0) {
            if(nums[index] == nums[index + 1]) {
                v = {0, 1};
                return v;
            }
            else if(nums[index] != nums[index + 1]) {
                v = {index, index};
                return v;
            }
        }
        else if(index == nums.size() - 1) {
            if(nums[index - 1] == nums[index]) {
                v = {index - 1, index};
                return v;
            }
            else if(nums[index - 1] != nums[index]) {
                v = {index, index};
                return v;
            }
        }
        else {
            if(nums[index - 1] == nums[index]) {
                v = {index - 1, index};
                return v;
            }
            else if(nums[index + 1] == nums[index]) {
                v = {index, index + 1};
                return v;
            }
            else {
                v = {index, index};
                return v;
            }
        }
        return v = {-1, -1};
    }
};

int main() {
    vector<int> v = {5,7,7,8,8,10};
    int target = 6;

    Solution soln;
    vector<int> result = soln.searchRange(v, target);
    cout << result[0] << " and " << result[1]; 
}