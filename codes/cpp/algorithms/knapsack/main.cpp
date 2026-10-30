#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, limit, i, c, w, v;
    int dp[101] = {}, un[101] = {};

    cin >> n >> limit;
    for (i = 0; i < n; ++i) {
        cin >> w >> v;
        // 큰 용량부터 갱신하여 같은 물건의 중복 선택 방지
        for (c = limit; c >= w; --c) {
            dp[c] = max(dp[c], dp[c - w] + v);
        }
        // 작은 용량부터 갱신하여 같은 종류를 다시 선택
        for (c = w; c <= limit; ++c) {
            un[c] = max(un[c], un[c - w] + v);
        }
    }
    cout << dp[limit] << '\n' << un[limit] << '\n';
}
