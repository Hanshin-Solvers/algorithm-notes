#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, i, j, area;
    vector<pair<int, int>> v;

    cin >> n;
    v.resize(n);
    for (auto& [x, y] : v) {
        cin >> x >> y;
    }

    area = 0;
    for (i = 0; i < n; ++i) {
        j = (i + 1) % n;
        area += v[i].first * v[j].second - v[i].second * v[j].first;
    }
    area = abs(area);

    cout << area / 2;
    if (area % 2 == 0) cout << ".0\n";
    else cout << ".5\n";
}
