#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, r, i, j;
    int dp[31][31] = {};

    cin >> n >> r;
    for (i = 0; i <= n; ++i) {
        dp[i][0] = 1;
        dp[i][i] = 1;
        for (j = 1; j < i; ++j) {
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
        }
    }
    cout << dp[n][r] << '\n';
}
