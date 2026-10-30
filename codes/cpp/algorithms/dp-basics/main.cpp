#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i;
    int dp[21] = {};

    cin >> n;
    dp[0] = 1;
    dp[1] = 1;
    for (i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    cout << dp[n] << '\n';
}
