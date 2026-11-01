#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

vector<int> g[101];
int d[101];

int main() {
    int n, m, i, u, v;
    queue<int> q;

    cin >> n >> m;
    for (i = 0; i < m; ++i) {
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    fill(d, d + 101, -1);
    d[1] = 0;
    q.push(1);

    while (!q.empty()) {
        u = q.front();
        q.pop();
        for (int v : g[u]) {
            if (d[v] != -1) continue;
            // 큐에 넣을 때 거리와 방문 여부 기록
            d[v] = d[u] + 1;
            q.push(v);
        }
    }
    cout << d[n] << '\n';
}
