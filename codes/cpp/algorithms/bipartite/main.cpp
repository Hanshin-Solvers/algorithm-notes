#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> g;
vector<int> c;

int main() {
    int n, m, i, a, b, u;
    bool ok;
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
        // 아직 방문하지 않은 연결 요소마다 새 탐색 시작
        if (c[i] != -1) continue;
        c[i] = 0;
        q.push(i);
        while (!q.empty()) {
            u = q.front();
            q.pop();
            for (int v : g[u]) {
                if (c[v] == -1) {
                    // 인접한 정점에 반대 색 배정
                    c[v] = 1 - c[u];
                    q.push(v);
                }
                // 간선 양 끝의 색이 같으면 이분 그래프 조건 위반
                else if (c[v] == c[u]) ok = false;
            }
        }
    }

    cout << (ok ? "YES" : "NO") << '\n';
}
