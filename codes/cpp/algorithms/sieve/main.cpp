#include <iostream>
#include <algorithm>

using namespace std;

bool prime[10000];

int main() {
    int n, i, j;

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
