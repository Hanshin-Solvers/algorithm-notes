#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m, r, c, nr, nc, k, cnt;
    int dr[] = {-1, 0, 1, 0}, dc[] = {0, 1, 0, -1};

    cin >> n >> m >> r >> c;
    --r;
    --c;
    cnt = 0;

    for (k = 0; k < 4; ++k) {
        nr = r + dr[k];
        nc = c + dc[k];
        if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
        // 출력 번호는 1부터 시작
        cout << nr + 1 << ' ' << nc + 1 << '\n';
        ++cnt;
    }

    if (cnt == 0) cout << "NONE\n";
}
