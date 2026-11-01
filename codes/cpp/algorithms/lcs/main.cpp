#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int dp[101][101];

int main() {
    int n, m, i, j;
    // dp[i][j]: 두 문자열의 앞 i개와 앞 j개 문자로 만든 LCS 길이
    string a, b, ans;

    cin >> a >> b;
    n = a.size();
    m = b.size();

    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= m; ++j) {
            // 문자가 같으면 두 문자열에서 함께 선택
            if (a[i - 1] == b[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    // 마지막 칸에서 문자를 선택하거나 길이가 유지되는 칸으로 이동
    i = n;
    j = m;
    while (i > 0 && j > 0) {
        // 문자가 같으면 두 문자열에서 함께 선택
        if (a[i - 1] == b[j - 1]) {
            ans += a[i - 1];
            --i;
            --j;
        }
        else if (dp[i - 1][j] >= dp[i][j - 1]) --i;
        else --j;
    }
    // 뒤에서부터 모은 문자를 뒤집어 원래 순서 복원
    reverse(ans.begin(), ans.end());

    cout << dp[n][m] << '\n';
    cout << ans << '\n';
}
