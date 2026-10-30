#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k, i, s, ans;
    vector<int> v;

    cin >> n >> k;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }
    s = 0;
    for (i = 0; i < k; ++i) {
        s += v[i];
    }
    ans = s;
    for (i = k; i < n; ++i) {
        s -= v[i - k];
        s += v[i];
        ans = max(ans, s);
    }
    cout << ans << '\n';
}
