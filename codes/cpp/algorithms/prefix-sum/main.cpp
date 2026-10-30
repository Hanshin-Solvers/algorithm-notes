#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, q, i, x, l, r;
    int p[1001] = {};

    cin >> n >> q;
    for (i = 1; i <= n; ++i) {
        cin >> x;
        p[i] = p[i - 1] + x;
    }
    for (i = 0; i < q; ++i) {
        cin >> l >> r;
        cout << p[r] - p[l - 1] << '\n';
    }
}
