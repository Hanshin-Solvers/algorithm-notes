#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int main() {
    int n, target, i, l, r, s, ans;

    cin >> n >> target;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }
    l = 0;
    s = 0;
    ans = n + 1;
    for (r = 0; r < n; ++r) {
        s += v[r];
        while (s >= target) {
            ans = min(ans, r - l + 1);
            s -= v[l];
            ++l;
        }
    }
    if (ans == n + 1) ans = 0;
    cout << ans << '\n';
}
