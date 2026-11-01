#include <iostream>
#include <vector>
#include <utility>

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
    // 임의의 정점에서 가장 먼 정점을 찾아 지름의 한 끝점 선택
    dfs(1, 0, 0);
    a = far;
    best = 0;
    // 찾은 끝점에서 다시 가장 먼 정점까지의 거리를 구해 지름 계산
    dfs(a, 0, 0);

    cout << best << '\n';
}
