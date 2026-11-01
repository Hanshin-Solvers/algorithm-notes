#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int d[101];

int main() {
    int a, b, x;
    queue<int> q;

    cin >> a >> b;
    fill(d, d + 101, -1);
    d[a] = 0;
    q.push(a);

    while (!q.empty()) {
        x = q.front();
        q.pop();
        for (int y : {x + 1, x * 2}) {
            if (y > 100 || d[y] != -1) continue;
            // 처음 도달한 횟수가 최소 연산 횟수임
            d[y] = d[x] + 1;
            q.push(y);
        }
    }
    cout << d[b] << '\n';
}
