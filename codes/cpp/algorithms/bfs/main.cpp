#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, i, j, x, y, nx, ny, k;
    int dx[4] = {-1, 1, 0, 0}, dy[4] = {0, 0, -1, 1};
    int d[30][30];
    string g[30];
    queue<pair<int, int>> q;

    cin >> n >> m;
    for (i = 0; i < n; ++i) {
        cin >> g[i];
        for (j = 0; j < m; ++j) {
            d[i][j] = -1;
        }
    }
    d[0][0] = 0;
    q.push({0, 0});

    while (!q.empty()) {
        x = q.front().first;
        y = q.front().second;
        q.pop();
        for (k = 0; k < 4; ++k) {
            nx = x + dx[k];
            ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (g[nx][ny] == '0' || d[nx][ny] != -1) continue;
            d[nx][ny] = d[x][y] + 1;
            q.push({nx, ny});
        }
    }
    cout << d[n - 1][m - 1] << '\n';
}
