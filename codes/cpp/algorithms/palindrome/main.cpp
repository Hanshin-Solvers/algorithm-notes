#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    int l, r;
    bool ok;

    cin >> s;
    l = 0;
    r = (int)s.size() - 1;
    ok = true;

    while (l < r) {
        if (s[l] != s[r]) {
            ok = false;
            break;
        }
        ++l;
        --r;
    }

    cout << (ok ? "YES" : "NO") << '\n';
}
