#include <iostream>
#include <cstddef>

using namespace std;

int main() {
    int n, i, x;

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (i = 0; i < n; ++i) {
        cin >> x;
        cout << x * 2 << '\n';
    }
}
