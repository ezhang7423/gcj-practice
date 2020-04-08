#include <iostream>
#include <vector>

using namespace std;
//  int maxProduct(int* nums, int len) {
//         int ans = nums[0];
//         int pre = 1;
//         int post = 1;
//         int tmp;
//         for (int i = 0; i < len; i++) {
//             l *= A[i];
//             r *= A[len - i - 1];
//             tmp = max(l, r);
//             res = max(tmp, res);
//         }
//         return res;
//     }

int maxProduct(int *nums, int len)
{
    int ans = nums[0];
    int pre = 0;
    int post = 0;
    int tmp;
    for (int i = 0; i < len; i++)
    {
        if (pre == 0)
        {
            pre = nums[i];
        }
        else
        {
            pre *= nums[i];
        }
        if (post == 0)
        {
            post = nums[len - i - 1];
        }
        else
        {

            post *= nums[len - i - 1];
        }
        tmp = max(pre, post);
        ans = max(tmp, ans);
    }
    return ans;
};

int main()
{
    vector<int> test = {-3, 0, 1, -2};
    cout << maxProduct(test) << endl;
}