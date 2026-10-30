#include <bits/stdc++.h>

using namespace std;

int main() {
    const int INF = 1000000;
    int n, m, s, t, i, a, b, w, u, du;
    vector<vector<pair<int, int>>> g;
    vector<int> d, p, ans;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    cin >> n >> m >> s >> t;
    g.resize(n + 1);
    d.assign(n + 1, INF);
    p.assign(n + 1, 0);
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        g[a].push_back({b, w});
    }
    d[s] = 0;
    pq.push({0, s});

    while (!pq.empty()) {
        du = pq.top().first;
        u = pq.top().second;
        pq.pop();
        if (du != d[u]) continue;
        for (const auto& [v, cost] : g[u]) {
            if (du + cost < d[v]) {
                d[v] = du + cost;
                p[v] = u;
                pq.push({d[v], v});
            }
        }
    }

    if (d[t] == INF) cout << -1 << '\n';
    else {
        for (u = t; u != 0; u = p[u]) {
            ans.push_back(u);
        }
        reverse(ans.begin(), ans.end());
        cout << d[t] << '\n';
        for (int v : ans) {
            cout << v << ' ';
        }
        cout << '\n';
    }
}
