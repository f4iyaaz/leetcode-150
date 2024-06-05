#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
        if(nums.size() == 1 || nums[0] > nums[1]) {
            return 0;
        }
        int low = 0;
        int high = nums.size() - 1;
        int mid = (low + high) / 2;

        while(low < high) {
            if(nums[mid] > nums[mid + 1] && nums[mid] > nums[mid - 1]) {
                return mid;
            }
            else if(nums[mid] < nums[mid + 1]){
                low = mid + 1;
                mid = (low + high) / 2;

            }
            else if(nums[mid] < nums[mid - 1]){
                high = mid - 1;
                mid = (low + high) / 2;
            }
        }
        if(nums[low] > nums[low - 1]) {
            return low;
        }
        return -1;
    
    
    
    }
    
};

int main() {
    vector<int> v = {1,2,3,1};
    Solution soln;
    cout << soln.findPeakElement(v);
}