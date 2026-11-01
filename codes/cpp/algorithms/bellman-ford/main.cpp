#include <iostream>
#include <vector>

using namespace std;

struct edge {
    int a, b, w;
};

vector<edge> edges;
vector<int> d;

int main() {
    const int INF = 1000000;
    int n, m, i, j, a, b, w;
    bool changed, cycle;

    cin >> n >> m;
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        edges.push_back({a, b, w});
    }
    d.assign(n + 1, INF);
    d[1] = 0;
    cycle = false;

    for (i = 1; i <= n; ++i) {
        changed = false;
        for (const auto& e : edges) {
            a = e.a;
            b = e.b;
            w = e.w;
            // 시작점에서 도달한 정점의 간선만 사용
            if (d[a] == INF) continue;
            if (d[a] + w < d[b]) {
                d[b] = d[a] + w;
                changed = true;
                // n번째 반복에도 갱신되면 시작점에서 도달 가능한 음수 사이클 존재
                if (i == n) cycle = true;
            }
        }
        // 거리 변화가 없으면 이후 반복에서도 갱신되지 않으므로 종료
        if (!changed) break;
    }

    if (cycle) cout << "NEGATIVE CYCLE\n";
    else {
        for (j = 1; j <= n; ++j) {
            if (d[j] == INF) cout << "INF ";
            else cout << d[j] << ' ';
        }
        cout << '\n';
    }
}
