#include <bits/stdc++.h>

using namespace std;

int main() {
    const int INF = 1000000;
    int n, m, i, j, a, b, w;
    bool changed, cycle;
    vector<array<int, 3>> edges;
    vector<int> d;

    cin >> n >> m;
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        edges.push_back({a, b, w});
    }
    d.assign(n + 1, INF);
    d[1] = 0;
    cycle = false;

    for (i = 1; i <= n; ++i) {
        changed = false;
        for (const auto& e : edges) {
            a = e[0];
            b = e[1];
            w = e[2];
            if (d[a] == INF) continue;
            if (d[a] + w < d[b]) {
                d[b] = d[a] + w;
                changed = true;
                if (i == n) cycle = true;
            }
        }
        if (!changed) break;
    }

    if (cycle) cout << "NEGATIVE CYCLE\n";
    else {
        for (j = 1; j <= n; ++j) {
            if (d[j] == INF) cout << "INF ";
            else cout << d[j] << ' ';
        }
        cout << '\n';
    }
}
