#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, i, a, b, u;
    vector<vector<int>> g;
    vector<int> d, ans;
    priority_queue<int, vector<int>, greater<int>> pq;

    cin >> n >> m;
    g.resize(n + 1);
    d.assign(n + 1, 0);
    for (i = 0; i < m; ++i) {
        cin >> a >> b;
        g[a].push_back(b);
        ++d[b];
    }
    for (i = 1; i <= n; ++i) {
        if (d[i] == 0) pq.push(i);
    }

    while (!pq.empty()) {
        u = pq.top();
        pq.pop();
        ans.push_back(u);
        for (int v : g[u]) {
            --d[v];
            if (d[v] == 0) pq.push(v);
        }
    }

    if ((int)ans.size() != n) cout << "IMPOSSIBLE\n";
    else {
        for (int v : ans) {
            cout << v << ' ';
        }
        cout << '\n';
    }
}
