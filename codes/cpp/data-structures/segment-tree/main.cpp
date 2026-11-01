#include <iostream>
#include <string>

using namespace std;

const int N = 10000; // 최대 원소 수
int t[N * 4];

// 노드 k의 담당 구간 [s, e)에서 인덱스 i의 값을 x로 갱신
void update(int k, int s, int e, int i, int x) {
    int m;

    // 원소 하나를 담당하는 리프 노드 갱신
    if (e - s == 1) {
        t[k] = x;
        return;
    }

    m = (s + e) / 2;
    if (i < m) update(k * 2, s, m, i, x);
    else update(k * 2 + 1, m, e, i, x);

    // 자식 구간의 합으로 부모 구간의 합 갱신
    t[k] = t[k * 2] + t[k * 2 + 1];
}

// [l, r) 구간 합 질의
int query(int k, int s, int e, int l, int r) {
    int m;

    // 질의 구간과 겹치지 않으면 합에 영향을 주지 않는 0 반환
    if (r <= s || e <= l) return 0;
    // 담당 구간이 질의 구간에 포함되면 저장된 합을 바로 반환
    if (l <= s && e <= r) return t[k];

    m = (s + e) / 2;
    return query(k * 2, s, m, l, r) + query(k * 2 + 1, m, e, l, r);
}

int main() {
    int n, q, i, j, l, r, x;
    string op;

    cin >> n >> q;

    // 루트 1에서 [0, n) 구간을 기준으로 입력값 저장
    for (i = 0; i < n; ++i) {
        cin >> x;
        update(1, 0, n, i, x);
    }

    for (i = 0; i < q; ++i) {
        cin >> op;

        if (op == "set") {
            cin >> j >> x;

            update(1, 0, n, j, x);
        }
        else {
            cin >> l >> r;

            cout << query(1, 0, n, l, r) << '\n';
        }
    }
}
