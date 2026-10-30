#include <bits/stdc++.h>

using namespace std;

int main() {
    string s, p;
    int n, m, i, j;
    vector<int> ans;

    cin >> s >> p;
    n = (int)s.size();
    m = (int)p.size();

    for (i = 0; i + m <= n; ++i) {
        j = 0;
        while (j < m && s[i + j] == p[j]) {
            ++j;
        }
        if (j == m) ans.push_back(i);
    }

    cout << ans.size() << '\n';
    for (int x : ans) {
        cout << x << ' ';
    }
    cout << '\n';
}
