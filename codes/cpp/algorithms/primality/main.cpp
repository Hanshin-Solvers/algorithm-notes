#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i;
    bool ok;

    cin >> n;
    ok = n >= 2;
    for (i = 2; i <= n / i; ++i) {
        if (n % i == 0) ok = false;
    }

    cout << (ok ? "YES" : "NO") << '\n';
}
