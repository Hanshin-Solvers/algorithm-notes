#include <bits/stdc++.h>

using namespace std;

int cross(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
    return (b.first - a.first) * (c.second - a.second)
         - (b.second - a.second) * (c.first - a.first);
}

int main() {
    int n;
    vector<pair<int, int>> v, lo, hi, ans;

    cin >> n;
    v.resize(n);
    for (auto& [x, y] : v) {
        cin >> x >> y;
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());

    if (v.size() == 1) ans = v;
    else {
        // 아래쪽 경계 구성
        for (const auto& pt : v) {
            while (lo.size() >= 2 && cross(lo[lo.size() - 2], lo.back(), pt) <= 0) {
                lo.pop_back();
            }
            lo.push_back(pt);
        }
        reverse(v.begin(), v.end());
        // 위쪽 경계 구성
        for (const auto& pt : v) {
            while (hi.size() >= 2 && cross(hi[hi.size() - 2], hi.back(), pt) <= 0) {
                hi.pop_back();
            }
            hi.push_back(pt);
        }
        lo.pop_back();
        hi.pop_back();
        ans = lo;
        ans.insert(ans.end(), hi.begin(), hi.end());
    }

    cout << ans.size() << '\n';
    for (const auto& [x, y] : ans) {
        cout << x << ' ' << y << '\n';
    }
}
