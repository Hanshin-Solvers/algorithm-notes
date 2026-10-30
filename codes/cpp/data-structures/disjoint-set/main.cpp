#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const int N = 10000;
int p[N + 1], sz[N + 1];

int find(int x) {
    while (p[x] != x) {
        p[x] = p[p[x]]; // 경로 절반 압축
        x = p[x];
    }
    return x;
}

// Union by Size: 집합의 원소 수를 기준으로 합침
void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (sz[a] < sz[b]) swap(a, b);
    p[b] = a;
    sz[a] += sz[b]; // 합친 집합의 원소 수 갱신
}

int main() {
    int n, q, i, a, b;
    string op;

    cin >> n >> q;

    for (i = 1; i <= n; ++i) {
        p[i] = i;
        sz[i] = 1;
    }

    for (i = 0; i < q; ++i) {
        cin >> op >> a;

        if (op == "size") cout << sz[find(a)] << '\n';
        else {
            cin >> b;

            if (op == "union") unite(a, b);
            else if (find(a) == find(b)) cout << "YES\n";
            else cout << "NO\n";
        }
    }
}
