#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(n > 0 && n <= m) {
            int tonight = m, k = 0;
            for(auto i = nums1.begin() + m; i != nums1.end(); i++) {
                nums1[tonight] = nums2[k];
                tonight++;
                k++;
            }
            sort(nums1.begin(), nums1.begin() + nums1.size());
            // print array
            // for(auto i = nums1.begin(); i != nums1.end(); i++) {
                // cout << *i << ", ";
            // }
        }
        else if(n > m) {
            int hey = m;
            for(auto i = nums2.begin(); i != nums2.end(); i++) {
                nums1[hey] = *i;
                hey++;
            }
        }
        sort(nums1.begin(), nums1.begin() + nums1.size());
        // // print array
        //     for(auto i = nums1.begin(); i != nums1.end(); i++) {
        //         cout << *i << ", ";
        //     }
    }
};

int main() {
    vector<int> v1 = {0};
    vector<int> v2 = {1};
    int m = 0, n = 1;
    Solution soln;
    soln.merge(v1, m, v2, n);
}