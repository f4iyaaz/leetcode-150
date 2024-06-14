#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
         vector<int> result = {-1, -1};
        int low = 0;
        int high = nums.size() - 1;

        if (nums.empty())
            return result;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                result[0] = mid;
                result[1] = mid;

                // Expand the range to the left
                while (result[0] > 0 && nums[result[0] - 1] == target)
                    result[0]--;

                // Expand the range to the right
                while (result[1] < nums.size() - 1 && nums[result[1] + 1] == target)
                    result[1]++;

                return result;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return result;
    }
};

int main() {
    vector<int> v = {5,7,7,8,8,10};
    int target = 6;

    Solution soln;
    vector<int> result = soln.searchRange(v, target);
    cout << result[0] << " and " << result[1]; 
}
