#include <iostream>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

vector<vector<int>> g;
vector<int> d, ans;

int main() {
    int n, m, i, a, b, u;
    priority_queue<int, vector<int>, greater<int>> pq;

    cin >> n >> m;
    g.resize(n + 1);
    d.assign(n + 1, 0);
    for (i = 0; i < m; ++i) {
        cin >> a >> b;
        g[a].push_back(b);
        // d[v]: 아직 처리하지 않은 진입 간선의 수
        ++d[b];
    }
    for (i = 1; i <= n; ++i) {
        // 선행 조건이 없는 정점을 넣고 작은 번호부터 선택
        if (d[i] == 0) pq.push(i);
    }

    while (!pq.empty()) {
        u = pq.top();
        pq.pop();
        ans.push_back(u);
        for (int v : g[u]) {
            // 현재 정점에서 나가는 간선을 제거하여 다음 정점의 진입 차수 감소
            --d[v];
            if (d[v] == 0) pq.push(v);
        }
    }

    // 모든 정점을 처리하지 못했으면 방향 사이클 존재
    if ((int)ans.size() != n) cout << "IMPOSSIBLE\n";
    else {
        for (int v : ans) {
            cout << v << ' ';
        }
        cout << '\n';
    }
}
