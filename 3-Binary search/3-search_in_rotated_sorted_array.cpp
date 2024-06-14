#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid = (low + high) / 2;

        if(nums.size() == 1) {
            if(nums[0] == target){
                return 0;
            }
            else {
                return -1;
            }
        }
        else {
            while(low <= high) {
                if(target == nums[mid]) {
                    return mid;
                }
                // left sorted portion
                else if(nums[low] <= nums[mid]) {
                    if(target < nums[low] || target > nums[mid]) {
                        low = mid + 1;
                        mid = (low + high) / 2;
                    }
                    else {
                        high = mid - 1;
                        mid = (low + high) / 2;
                    }
                }
                // right sorted portion
                else {
                    if(target < nums[mid] || target > nums[high]) {
                        high = mid - 1;
                        mid = (low + high) / 2;
                    }
                    else {
                        low = mid + 1;
                        mid = (low + high) / 2;
                    }
                }
            }
        }
        return -1;
    }
};

int main() {
    vector<int> v = {5,1,2,3,4};
    // vector<int> v = {4,5,6,7,0,1,2};
    // vector<int> v = {1};
    int target = 5;
    Solution soln;
    cout << soln.search(v, target);
}