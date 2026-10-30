#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, n, i, j, x, sum;

    cin >> t;
    for (i = 0; i < t; ++i) {
        cin >> n;
        // 케이스마다 합 초기화
        sum = 0;
        for (j = 0; j < n; ++j) {
            cin >> x;
            sum += x;
        }
        cout << sum << '\n';
    }
}
