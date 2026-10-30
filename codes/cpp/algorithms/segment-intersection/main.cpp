#include <bits/stdc++.h>

using namespace std;

int cross(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
    return (b.first - a.first) * (c.second - a.second)
         - (b.second - a.second) * (c.first - a.first);
}

int sign(int x) {
    if (x > 0) return 1;
    else if (x == 0) return 0;
    else return -1;
}

bool overlap(int a, int b, int c, int d) {
    return max(min(a, b), min(c, d)) <= min(max(a, b), max(c, d));
}

int main() {
    pair<int, int> a, b, c, d;
    int x, y, z, w;
    bool ok;

    cin >> a.first >> a.second >> b.first >> b.second;
    cin >> c.first >> c.second >> d.first >> d.second;
    x = sign(cross(a, b, c));
    y = sign(cross(a, b, d));
    z = sign(cross(c, d, a));
    w = sign(cross(c, d, b));

    if (x == 0 && y == 0 && z == 0 && w == 0) {
        ok = overlap(a.first, b.first, c.first, d.first)
          && overlap(a.second, b.second, c.second, d.second);
    }
    else ok = (x * y <= 0 && z * w <= 0);

    cout << (ok ? "YES" : "NO") << '\n';
}
