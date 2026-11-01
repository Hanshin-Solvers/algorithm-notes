#include <iostream>
#include <vector>

using namespace std;

vector<int> g[101];
bool seen[101];

void dfs(int u) {
    // 다른 정점으로 이동하기 전에 방문을 표시하여 사이클의 재방문 방지
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
        // 미방문 정점에서 시작한 DFS 하나가 연결 요소 하나를 탐색함
        if (!seen[i]) {
            ++cnt;
            dfs(i);
        }
    }
    cout << cnt << '\n';
}
