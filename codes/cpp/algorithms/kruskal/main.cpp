#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

struct edge {
    int a, b, w;
};

int p[101], sz[101];
vector<edge> edges;

bool compare(const edge& x, const edge& y) {
    return x.w < y.w;
}

int find(int x) {
    while (x != p[x]) {
        // 조부모로 연결하여 대표까지의 경로 단축
        p[x] = p[p[x]];
        x = p[x];
    }
    return x;
}

bool unite(int a, int b) {
    a = find(a);
    b = find(b);
    // 이미 같은 집합이면 간선 추가 시 사이클이 생기므로 제외
    if (a == b) return false;
    // 작은 집합을 큰 집합 아래에 연결하도록 대표 교환
    if (sz[a] < sz[b]) swap(a, b);
    p[b] = a;
    sz[a] += sz[b];
    return true;
}

int main() {
    int n, m, i, a, b, w, cnt, ans;

    cin >> n >> m;
    for (i = 1; i <= n; ++i) {
        p[i] = i;
        sz[i] = 1;
    }
    for (i = 0; i < m; ++i) {
        cin >> a >> b >> w;
        edges.push_back({a, b, w});
    }
    // 가중치가 작은 간선부터 검사
    sort(edges.begin(), edges.end(), compare);
    cnt = 0;
    ans = 0;

    for (const auto& e : edges) {
        if (unite(e.a, e.b)) {
            ans += e.w;
            ++cnt;
        }
    }

    // n-1개 간선을 선택했으면 모든 정점을 연결한 신장 트리 완성
    if (cnt == n - 1) cout << ans << '\n';
    else cout << "IMPOSSIBLE\n";
}
