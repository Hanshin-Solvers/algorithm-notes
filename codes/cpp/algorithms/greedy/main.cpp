#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i, cnt, end;
    vector<pair<int, int>> v, merged;

    cin >> n;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }
    sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });
    cnt = 0;
    end = 0;
    for (const auto& [s, e] : v) {
        if (s >= end) {
            ++cnt;
            end = e;
        }
    }

    // 시작점 순서로 구간 병합
    sort(v.begin(), v.end());
    for (const auto& [s, e] : v) {
        if (merged.empty() || merged.back().second < s) merged.push_back({s, e});
        else merged.back().second = max(merged.back().second, e);
    }
    cout << cnt << '\n' << merged.size() << '\n';
    for (const auto& [s, e] : merged) {
        cout << s << ' ' << e << '\n';
    }
}
