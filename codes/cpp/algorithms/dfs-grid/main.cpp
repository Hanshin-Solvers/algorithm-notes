#include <iostream>

using namespace std;

int n, m;
int dr[] = {-1, 0, 1, 0}, dc[] = {0, 1, 0, -1};
int g[20][20];
bool seen[20][20];

void dfs(int r, int c) {
    int k, nr, nc;

    seen[r][c] = true;
    for (k = 0; k < 4; ++k) {
        nr = r + dr[k];
        nc = c + dc[k];
        // 범위 확인 후 벽과 방문 여부 확인
        if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
        if (g[nr][nc] == 0 || seen[nr][nc]) continue;
        dfs(nr, nc);
    }
}

int main() {
    int i, j, cnt;

    cin >> n >> m;
    for (i = 0; i < n; ++i) {
        for (j = 0; j < m; ++j) {
            cin >> g[i][j];
        }
    }
    cnt = 0;

    for (i = 0; i < n; ++i) {
        for (j = 0; j < m; ++j) {
            if (g[i][j] == 1 && !seen[i][j]) {
                // 새 영역 탐색
                ++cnt;
                dfs(i, j);
            }
        }
    }
    cout << cnt << '\n';
}
