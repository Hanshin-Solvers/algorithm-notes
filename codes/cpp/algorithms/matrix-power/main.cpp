#include <bits/stdc++.h>

using namespace std;

int n;

vector<vector<int>> mul(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    int i, j, k;
    vector<vector<int>> c(n, vector<int>(n));

    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            for (k = 0; k < n; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return c;
}

vector<vector<int>> power(const vector<vector<int>>& a, int b) {
    int i;
    vector<vector<int>> t;

    if (b == 0) {
        t.assign(n, vector<int>(n));
        for (i = 0; i < n; ++i) {
            t[i][i] = 1;
        }
        return t;
    }
    t = power(a, b / 2);
    t = mul(t, t);
    if (b % 2 == 1) t = mul(t, a);
    return t;
}

int main() {
    int b, i, j;
    vector<vector<int>> a, t;

    cin >> n >> b;
    a.assign(n, vector<int>(n));
    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
    }
    t = power(a, b);

    for (const auto& row : t) {
        for (int x : row) {
            cout << x << ' ';
        }
        cout << '\n';
    }
}
