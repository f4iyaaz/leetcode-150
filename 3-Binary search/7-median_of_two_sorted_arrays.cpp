#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        // merge the two arrays
        int m = nums2.size();
        for(int i = 0; i < m; i++) {
            nums1.push_back(nums2[i]);
        }

        int low = 0;
        int high = nums1.size() - 1;
        int mid = (low + high) / 2;
        
        sort(nums1.begin(), nums1.begin() + nums1.size());

        if(nums1.size() % 2 != 0) {
            double res = static_cast<double>(nums1[mid]);
            return res;
        }
        else {
            // cout << nums1.size() << "\n";
            // cout << nums1[mid] << "\n";
            double res = static_cast<double>(nums1[mid] + nums1[mid + 1]) / 2.0;
            return res;
        }

    }
};

int main() {

    vector<int> v1 = {1, 2};
    vector<int> v2 = {3, 4};
    Solution sol;

    double result = sol.findMedianSortedArrays(v1, v2);
    cout << result;
}