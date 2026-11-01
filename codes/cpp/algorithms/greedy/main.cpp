#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
    // 종료 시각 오름차순
    return a.second < b.second;
}

vector<pair<int, int>> v;

int main() {
    int n, i, cnt, end;

    cin >> n;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }

    sort(v.begin(), v.end(), compare);
    cnt = 0;
    end = 0;
    for (const auto& [s, e] : v) {
        if (s >= end) {
            ++cnt;
            end = e;
        }
    }

    cout << cnt << '\n';
}
