#include <iostream>

using namespace std;

int main() {
    int n, r, i, p, f;

    cin >> n >> r;
    p = 1;
    f = 1;
    for (i = 0; i < r; ++i) {
        p *= n - i;
        f *= i + 1;
    }

    cout << p << ' ' << p / f << '\n';
}
