#include <iostream>
#include <queue>
#include <utility>

using namespace std;

int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
int d[30][30], g[30][30];

int main() {
    int n, m, i, j, x, y, nx, ny, k;
    queue<pair<int, int>> q;

    cin >> n >> m;
    for (i = 0; i < n; ++i) {
        for (j = 0; j < m; ++j) {
            cin >> g[i][j];
            d[i][j] = -1;
        }
    }
    // d[x][y]: 시작 칸에서의 최소 이동 횟수, -1은 미방문
    d[0][0] = 0;
    q.push({0, 0});

    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (k = 0; k < 4; ++k) {
            nx = x + dx[k];
            ny = y + dy[k];
            // 배열에 접근하기 전에 다음 칸이 격자 안인지 확인
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (g[nx][ny] == 0 || d[nx][ny] != -1) continue;
            // 처음 발견한 거리가 최단 거리이므로 큐에 넣기 전에 방문 처리
            d[nx][ny] = d[x][y] + 1;
            q.push({nx, ny});
        }
    }
    cout << d[n - 1][m - 1] << '\n';
}
