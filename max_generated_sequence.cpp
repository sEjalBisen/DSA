#include<bits/stdc++.h>
using namespace std;

class solution{
    public:
    int maxInGeneratedSequence(int n) {
        if (n < 2) return n;
        vector<int> nums;
        nums.push_back(0);
        nums.push_back(1);
        int max = INT_MIN;
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                nums.push_back(nums[i / 2]);
            } else {
                int ele = nums[i / 2] + nums[i / 2 + 1];
                nums.push_back(ele);
            }
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        return max;
    }
};