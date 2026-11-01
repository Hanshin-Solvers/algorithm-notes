#include <iostream>

using namespace std;

int d[102];

int main() {
    int n, q, i, l, r, x, s;

    cin >> n >> q;
    for (i = 0; i < q; ++i) {
        cin >> l >> r >> x;
        d[l] += x;
        d[r + 1] -= x;
    }
    s = 0;
    for (i = 1; i <= n; ++i) {
        s += d[i];
        cout << s << ' ';
    }
    cout << '\n';
}
