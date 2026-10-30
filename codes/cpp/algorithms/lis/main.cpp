#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i, x, p;
    vector<int> v;

    cin >> n;
    for (i = 0; i < n; ++i) {
        cin >> x;
        p = lower_bound(v.begin(), v.end(), x) - v.begin();
        if (p == (int)v.size()) v.push_back(x);
        else v[p] = x;
    }
    cout << v.size() << '\n';
}
