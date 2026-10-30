#include <bits/stdc++.h>

using namespace std;

vector<int> g[101];
bool seen[101];

void dfs(int u) {
    seen[u] = true;
    for (int v : g[u]) {
        if (!seen[v]) dfs(v);
    }
}

int main() {
    int n, m, i, a, b, cnt;

    cin >> n >> m;
    for (i = 0; i < m; ++i) {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    cnt = 0;
    for (i = 1; i <= n; ++i) {
        if (!seen[i]) {
            ++cnt;
            dfs(i);
        }
    }
    cout << cnt << '\n';
}
