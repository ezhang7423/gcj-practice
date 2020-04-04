#include <iostream> // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <unordered_map>
using namespace std; // since cin and cout are both in namespace std, this saves some text
typedef unordered_map<int, int> di;

vector<int> confusion()
{
    vector<int> x{1, 2, 3, 4, 5};
    return x;
}

int main()
{

    vector<int> a = confusion();
    cout
        << a[4] << endl;
    return 0;
}