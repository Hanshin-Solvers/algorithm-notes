#include <iostream>

using namespace std;

int main() {
    int n, s, i, j, cnt;

    cin >> n >> s;
    cnt = 0;

    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= n; ++j) {
            if (i + j == s) ++cnt;
        }
    }

    cout << cnt << '\n';
}
