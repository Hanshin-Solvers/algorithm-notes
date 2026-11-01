#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<vector<int>> d;

int main() {
    const int INF = 1000000;
    int n, m, i, j, k, a, b, w;

    cin >> n >> m;
    d.assign(n + 1, vector<int>(n + 1, INF));
    for (i = 1; i <= n; ++i) {
        d[i][i] = 0;
    }
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        // 같은 두 정점 사이의 여러 간선 중 최소 가중치 저장
        d[a][b] = min(d[a][b], w);
    }

    // 경유 가능한 정점을 k까지 확장하므로 k를 가장 바깥에서 순회
    for (k = 1; k <= n; ++k) {
        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= n; ++j) {
                // i에서 k 또는 k에서 j로 갈 수 없으면 경로 결합 제외
                if (d[i][k] == INF || d[k][j] == INF) continue;
                // 기존 거리와 i → k → j 경로의 거리 비교
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    for (i = 1; i <= n; ++i) {
        for (j = 1; j <= n; ++j) {
            if (d[i][j] == INF) cout << -1 << ' ';
            else cout << d[i][j] << ' ';
        }
        cout << '\n';
    }
}
