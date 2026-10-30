#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i, j;
    bool prime[10000];

    cin >> n;
    fill(prime, prime + n + 1, true);
    prime[0] = false;
    prime[1] = false;
    for (i = 2; i * i <= n; ++i) {
        if (prime[i]) {
            for (j = i * i; j <= n; j += i) {
                prime[j] = false;
            }
        }
    }

    for (i = 2; i <= n; ++i) {
        if (prime[i]) cout << i << ' ';
    }
    cout << '\n';
}
