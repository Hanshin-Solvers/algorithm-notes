#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i;
    vector<pair<int, int>> v;

    cin >> n;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }
    // 점수 내림차순, 번호 오름차순
    sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });

    for (const auto& [id, score] : v) {
        cout << id << ' ';
    }
    cout << '\n';
}
