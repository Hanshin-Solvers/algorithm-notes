#include <bits/stdc++.h>

using namespace std;

int a[101], t[101];

void sortRange(int l, int r) {
    int m, i, j, k;

    if (r - l <= 1) return;
    m = (l + r) / 2;
    sortRange(l, m);
    sortRange(m, r);

    i = l;
    j = m;
    k = l;
    while (i < m && j < r) {
        if (a[i] <= a[j]) {
            t[k] = a[i];
            ++i;
        }
        else {
            t[k] = a[j];
            ++j;
        }
        ++k;
    }
    while (i < m) {
        t[k] = a[i];
        ++k;
        ++i;
    }
    while (j < r) {
        t[k] = a[j];
        ++k;
        ++j;
    }
    for (i = l; i < r; ++i) {
        a[i] = t[i];
    }
}

int main() {
    int n, i;

    cin >> n;
    for (i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sortRange(0, n);

    for (i = 0; i < n; ++i) {
        cout << a[i] << ' ';
    }
    cout << '\n';
}
