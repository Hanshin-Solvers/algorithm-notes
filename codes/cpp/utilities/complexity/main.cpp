#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i, j, cnt, pairs;

    cin >> n;
    cnt = 0;
    pairs = 0;

    // N번 실행
    for (i = 1; i <= n; ++i) {
        ++cnt;
    }

    // (N - 1) + (N - 2) + ... + 1번 실행
    for (i = 1; i <= n; ++i) {
        for (j = i + 1; j <= n; ++j) {
            ++pairs;
        }
    }

    cout << cnt << '\n' << pairs << '\n';
}
