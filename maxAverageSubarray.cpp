#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution
{
public:
    double findMaxAverage(vector<int> &nums, int k)
    {
        double current = 0;
        int n = nums.size();
        double ans = 0;

        // build the first window
        for (int i=0; i < k; i++) {
            current += (double)nums[i];
        }

        ans = current;
        int start = 0, end = k;
        while(end < n)
        {
            current += (double)nums[end];
            current -= (double)nums[start];
            cout << " current: ";
            cout << current;
            cout << " vs: ";
            cout << ans;
            start++; end++;
            ans = max(ans, current);
        }

        return ans/k;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 12, -5, -6, 50, 3};
    double ans = sol.findMaxAverage(nums, 4);
    cout << ans;
    return 0;
}