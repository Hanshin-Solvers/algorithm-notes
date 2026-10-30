#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b, x, y, r;

    cin >> a >> b;
    x = a;
    y = b;
    while (y != 0) {
        r = x % y;
        x = y;
        y = r;
    }

    cout << x << ' ' << a / x * b << '\n';
}
