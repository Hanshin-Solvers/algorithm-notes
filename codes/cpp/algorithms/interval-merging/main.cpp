#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
    // 시작점 오름차순, 시작점이 같으면 끝점 오름차순
    if (a.first != b.first) return a.first < b.first;
    return a.second < b.second;
}

vector<pair<int, int>> v, ans;

int main() {
    int n, i;

    cin >> n;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }

    // 시작점 순서로 정렬 후 병합
    sort(v.begin(), v.end(), compare);
    for (const auto& [s, e] : v) {
        if (ans.empty() || ans.back().second < s) ans.push_back({s, e});
        else ans.back().second = max(ans.back().second, e);
    }

    cout << ans.size() << '\n';
    for (const auto& [s, e] : ans) {
        cout << s << ' ' << e << '\n';
    }
}
