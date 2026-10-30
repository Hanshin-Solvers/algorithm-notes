#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> g[101];
int far, best;

void dfs(int u, int par, int dist) {
    if (dist > best) {
        best = dist;
        far = u;
    }
    for (const auto& [v, w] : g[u]) {
        if (v == par) continue;
        dfs(v, u, dist + w);
    }
}

int main() {
    int n, i, a, b, w;

    cin >> n;
    for (i = 0; i < n - 1; ++i) {
        cin >> a >> b >> w;
        g[a].push_back({b, w});
        g[b].push_back({a, w});
    }

    far = 1;
    best = 0;
    dfs(1, 0, 0);
    a = far;
    best = 0;
    dfs(a, 0, 0);

    cout << best << '\n';
}
