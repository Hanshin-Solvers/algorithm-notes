#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i;

    cin >> n;
    for (i = 2; i <= n / i; ++i) {
        while (n % i == 0) {
            cout << i << ' ';
            n /= i;
        }
    }
    if (n > 1) cout << n;
    cout << '\n';
}
