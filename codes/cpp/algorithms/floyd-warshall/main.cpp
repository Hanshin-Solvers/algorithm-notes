#include <bits/stdc++.h>

using namespace std;

int main() {
    const int INF = 1000000;
    int n, m, i, j, k, a, b, w;
    vector<vector<int>> d;

    cin >> n >> m;
    d.assign(n + 1, vector<int>(n + 1, INF));
    for (i = 1; i <= n; ++i) {
        d[i][i] = 0;
    }
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        d[a][b] = min(d[a][b], w);
    }

    for (k = 1; k <= n; ++k) {
        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= n; ++j) {
                if (d[i][k] == INF || d[k][j] == INF) continue;
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= n; ++j) {
            if (d[i][j] == INF) cout << -1 << ' ';
            else cout << d[i][j] << ' ';
        }
        cout << '\n';
    }
}
