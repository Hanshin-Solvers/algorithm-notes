#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int main() {
    int n, x, i, l, r;

    cin >> n >> x;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }
    l = lower_bound(v.begin(), v.end(), x) - v.begin();
    r = upper_bound(v.begin(), v.end(), x) - v.begin();
    cout << r - l << '\n';
}
