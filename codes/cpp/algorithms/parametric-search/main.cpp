#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k, i, l, r, m, cnt, ans;
    vector<int> v;

    cin >> n >> k;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }
    l = 1;
    r = *max_element(v.begin(), v.end());
    ans = 0;
    while (l <= r) {
        m = (l + r) / 2;
        cnt = 0;
        for (int x : v) {
            cnt += x / m;
        }
        if (cnt >= k) {
            ans = m;
            l = m + 1;
        }
        else r = m - 1;
    }
    cout << ans << '\n';
}
