#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, i, j;
    int dp[11][11] = {};
    string g[10];

    cin >> n >> m;
    for (i = 0; i < n; ++i) {
        cin >> g[i];
    }
    dp[1][1] = 1;
    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= m; ++j) {
            if (i == 1 && j == 1) continue;
            if (g[i - 1][j - 1] == '1') dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    cout << dp[n][m] << '\n';
}
