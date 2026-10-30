#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, i, a, b, u;
    bool ok;
    vector<vector<int>> g;
    vector<int> c;
    queue<int> q;

    cin >> n >> m;
    g.resize(n + 1);
    c.assign(n + 1, -1);
    for (i = 0; i < m; ++i) {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    ok = true;
    for (i = 1; i <= n; ++i) {
        if (c[i] != -1) continue;
        c[i] = 0;
        q.push(i);
        while (!q.empty()) {
            u = q.front();
            q.pop();
            for (int v : g[u]) {
                if (c[v] == -1) {
                    c[v] = 1 - c[u];
                    q.push(v);
                }
                else if (c[v] == c[u]) ok = false;
            }
        }
    }

    cout << (ok ? "YES" : "NO") << '\n';
}
