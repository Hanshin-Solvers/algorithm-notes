#include <iostream>

using namespace std;

int dp[21];

int main() {
    int n, i;

    cin >> n;

    // 피보나치 수열의 초기값
    dp[0] = 0;
    dp[1] = 1;
    for (i = 2; i <= n; ++i) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    cout << dp[n] << '\n';
}
