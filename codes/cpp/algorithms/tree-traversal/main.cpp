#include <bits/stdc++.h>

using namespace std;

vector<int> g[101];
int p[101], d[101], sz[101];

void dfs(int u, int par) {
    // 자식 탐색 전 부모와 크기 초기값 설정
    p[u] = par;
    sz[u] = 1;
    for (int v : g[u]) {
        if (v == par) continue;
        d[v] = d[u] + 1;
        dfs(v, u);
        // 자식 탐색 후 서브트리 크기 합산
        sz[u] += sz[v];
    }
}

int main() {
    int n, i, a, b;

    cin >> n;
    for (i = 0; i < n - 1; ++i) {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }

    dfs(1, 0);

    for (i = 1; i <= n; ++i) {
        cout << p[i] << ' ' << d[i] << ' ' << sz[i] << '\n';
    }
}
