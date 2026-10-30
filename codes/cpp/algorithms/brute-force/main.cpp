#include <bits/stdc++.h>

using namespace std;

int n, target, cnt;

void search(int d, int s) {
    int x;

    if (d == 2) {
        if (s == target) ++cnt;
        return;
    }
    for (x = 1; x <= n; ++x) {
        search(d + 1, s + x);
    }
}

int main() {
    cin >> n >> target;
    search(0, 0);
    cout << cnt << '\n';
}
