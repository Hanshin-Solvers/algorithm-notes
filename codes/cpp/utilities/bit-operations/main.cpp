#include <bits/stdc++.h>

using namespace std;

int main() {
    int x, k, mask, bit, on, off, flip;

    cin >> x >> k;
    mask = 1 << k;

    bit = (x >> k) & 1;
    on = x | mask;
    off = x & ~mask;
    flip = x ^ mask;

    cout << bit << ' ' << on << ' ' << off << ' ' << flip << '\n';
}
