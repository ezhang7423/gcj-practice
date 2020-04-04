#include <iostream> // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <math.h>
#include <unordered_map>
#include <string>
using namespace std; // since cin and cout are both in namespace std, this saves some text

typedef unordered_map<int, int> di;
typedef unordered_map<int, vector<int>> dl;

int **init(int sz)
{
    int **ans = new int *[sz];
    for (int i = 0; i < sz; i++)
    {
        ans[i] = new int[sz]{};
    }
    return ans;
}

string print(int **arr, int sz)
{
    string ans = "";
    for (int i = 0; i < sz; i++)
    {
        for (int j = 0; j < sz; j++)
        {
            ans += arr[i][j] + ' ';
        }
        ans += "\n";
    }
    return ans;
}

int *get_col(di arr, int n, int index)
{
    int *result = new int[n]{};
    int c = 0;
    for (int i = 0; i < n; i++)
    {
        if (n * i + index % n < index)
        {
            result[c] = arr[n * i + index % n];
            c++;
        }
    }
    return result;
}

int *get_row(di arr, int n, int index)
{
    int *result = new int[n]{};
    int c = 0;
    for (int i = 0; i < n; i++)
    {
        if (i + (index - index % n) < index)
        {
            result[c] = arr[i + (index - index % n)];
            c++;
        }
    }
    return result;
}

int sum_of_diag(di arr, int n)
{
    int result = 0;
    for (int i = 0; i < n - 1; i++)
    {
        result += arr[(n + 1) * i];
    }
    return result;
}

bool in(int n, int i, int *arr)
{
    for (int j = 0; i < n; i++)
    {
        if (arr[j] == i)
        {
            return true;
        }
    }
    return false;
}

vector<int> getPoss(di arr, int n, int i, int required_diag)
{
    vector<int> all_avails(n, 0);
    for (int i = 1; i <= n; i++)
    {
        all_avails[i] = i;
    }
    if (i == 0)
    {
        return all_avails;
    }
    int c = 0;
    vector<int> result(1 - n, 0);
    int *current_col = get_col(arr, n, i);
    int *current_row = get_row(arr, n, i);
    bool last_el = n * n - 1 == i;
    int sum_of_d = sum_of_diag(arr, n);
    for (int i = 0; i < n; i++)
    {
        bool c1 = (!(in(n, all_avails[i], current_col) || in(n, all_avails[i], current_row)));
        if (c1 && !last_el || (sum_of_d + all_avails[i] == required_diag))
        {
            result[c] = all_avails[i];
            c++;
        }
    }
    delete[] current_row;
    delete[] current_col;
    return result;
}
int **eval(int n, int required_diag)
{
    dl pos;
    di val;
    pos[0] = getPoss(val, n, 0, 0);
    val[0] = pos[0][0];
    int current_index, end;
    current_index = 0;
    end = n * n;

    while (current_index + 1 < end)
    {
        current_index += 1;
        pos[current_index] = getPoss(val, n, current_index, required_diag);
        if (pos[current_index][0] == 0)
        {
            while (true)
            {
                current_index -= 1;
                if (pos[current_index][1] != 0)
                {
                    break;
                }
                if (current_index < 0)
                {
                    return 0;
                }
            }
            pos[current_index].erase(pos[current_index].begin());
        }
        val[current_index] = pos[current_index][0];
    }
    int **arr = init(n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            arr[i][j] = val[n * i + j];
        }
    }
    return arr;
}

int main()
{

    int t, sz, tr;
    cin >> t; // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i)
    {
        cin >> sz >> tr; // read n and then m.

        int **ans = eval(sz, tr);
        if (ans == nullptr)
        {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << i << ": POSSIBLE" << endl;
        int temp = 0;
        cout << print(ans, sz);
    }

    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    return 0;
}
