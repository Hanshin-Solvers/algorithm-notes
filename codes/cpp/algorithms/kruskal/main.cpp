#include <bits/stdc++.h>

using namespace std;

int p[101], sz[101];

int find(int x) {
    while (x != p[x]) {
        p[x] = p[p[x]];
        x = p[x];
    }
    return x;
}

bool unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return false;
    if (sz[a] < sz[b]) swap(a, b);
    p[b] = a;
    sz[a] += sz[b];
    return true;
}

int main() {
    int n, m, i, a, b, w, cnt, ans;
    vector<array<int, 3>> edges;

    cin >> n >> m;
    for (i = 1; i <= n; ++i) {
        p[i] = i;
        sz[i] = 1;
    }
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        edges.push_back({w, a, b});
    }
    sort(edges.begin(), edges.end());
    cnt = 0;
    ans = 0;

    for (const auto& e : edges) {
        if (unite(e[1], e[2])) {
            ans += e[0];
            ++cnt;
        }
    }

    if (cnt == n - 1) cout << ans << '\n';
    else cout << "IMPOSSIBLE\n";
}
