#include <iostream>
#include <limits>
using namespace std;
// class Solution:
//     def maxSubArray(self, nums: [int]) -> int:
//         a, c = [-math.inf, 0]
//         for num in nums:
//             num = -num
//             if c <= 0:
//                 c = num
//             else:
//                 c += num
//             if c > a:
//                 a = c

//         return -a

// x = Solution()
// print(x.maxSubArray(
//     [1, -1, -20]))

double inf = std::numeric_limits<double>::infinity();
int minSubArray(int *arr, int len)
{
    float a = -inf;
    int c = 0;
    int num;
    for (int i = 0; i < len; i++)
    {
        cout << a << " " << c << " " << num << " " << endl;
        num = -arr[i];
        if (c <= 0)
        {
            c = num;
        }
        else
        {
            c += num;
        }
        if (c > a)
        {
            a = c;
        }
    }
    return -a;
}
int main()
{
    int *arr = new int[4]{1, 2, -3, 4};
    cout << minSubArray(arr, 4) << endl;
    ;
}