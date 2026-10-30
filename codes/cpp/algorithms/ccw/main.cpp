#include <bits/stdc++.h>

using namespace std;

int cross(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
    return (b.first - a.first) * (c.second - a.second)
         - (b.second - a.second) * (c.first - a.first);
}

int main() {
    pair<int, int> a, b, c;
    int v;

    cin >> a.first >> a.second;
    cin >> b.first >> b.second;
    cin >> c.first >> c.second;

    v = cross(a, b, c);
    if (v > 0) cout << 1 << '\n';
    else if (v == 0) cout << 0 << '\n';
    else cout << -1 << '\n';
}
