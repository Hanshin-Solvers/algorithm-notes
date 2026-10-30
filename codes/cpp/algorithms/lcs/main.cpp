#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, i, j;
    int dp[101][101] = {};
    string a, b;

    cin >> a >> b;
    n = a.size();
    m = b.size();
    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= m; ++j) {
            if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    cout << dp[n][m] << '\n';
}
