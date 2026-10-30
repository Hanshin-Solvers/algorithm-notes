#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, q, i, j, x, a, b, c, d;
    int p[31][31] = {};

    cin >> n >> m >> q;
    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= m; ++j) {
            cin >> x;
            p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + x;
        }
    }
    for (i = 0; i < q; ++i) {
        cin >> a >> b >> c >> d;
        cout << p[c][d] - p[a - 1][d] - p[c][b - 1] + p[a - 1][b - 1] << '\n';
    }
}
