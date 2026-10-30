#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i, x;

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (i = 0; i < n; ++i) {
        cin >> x;
        cout << x * 2 << '\n';
    }
}
