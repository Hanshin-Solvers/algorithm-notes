#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

bool compare(const pair<int, int>& a, const pair<int, int>& b) {
    // 점수 내림차순, 번호 오름차순
    if (a.second != b.second) return a.second > b.second;
    return a.first < b.first;
}

vector<pair<int, int>> v;

int main() {
    int n, i;

    cin >> n;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i].first >> v[i].second;
    }

    sort(v.begin(), v.end(), compare);

    for (const auto& [id, score] : v) {
        cout << id << ' ';
    }
    cout << '\n';
}
