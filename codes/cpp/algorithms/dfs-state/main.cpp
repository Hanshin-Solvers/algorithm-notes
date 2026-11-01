#include <iostream>

using namespace std;

bool seen[101];

void dfs(int x) {
    seen[x] = true;

    // 연산 결과가 범위 안이고 미방문 상태이면 탐색
    if (x + 1 <= 100 && !seen[x + 1]) dfs(x + 1);
    if (x * 2 <= 100 && !seen[x * 2]) dfs(x * 2);
}

int main() {
    int a, b;

    cin >> a >> b;
    dfs(a);

    if (seen[b]) cout << "YES\n";
    else cout << "NO\n";
}
