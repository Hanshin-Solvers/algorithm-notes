#include <iostream>

using namespace std;

struct point {
    int x, y;
};

int cross(const point& a, const point& b, const point& c) {
    return (b.x - a.x) * (c.y - a.y)
         - (b.y - a.y) * (c.x - a.x);
}

int main() {
    point a, b, c;
    int v;

    cin >> a.x >> a.y;
    cin >> b.x >> b.y;
    cin >> c.x >> c.y;

    v = cross(a, b, c);
    if (v > 0) cout << 1 << '\n';
    else if (v == 0) cout << 0 << '\n';
    else cout << -1 << '\n';
}
