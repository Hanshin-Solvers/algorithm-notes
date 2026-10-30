#include <bits/stdc++.h>

using namespace std;

int n, r;
int a[9];

void search(int d, int start) {
    int i;

    if (d == r) {
        for (i = 0; i < r; ++i) {
            cout << a[i] << ' ';
        }
        cout << '\n';
        return;
    }
    // 남은 수로 필요한 자리를 채울 수 있을 때만 선택
    for (i = start; i <= n - (r - d) + 1; ++i) {
        a[d] = i;
        search(d + 1, i + 1);
    }
}

int main() {
    cin >> n >> r;
    search(0, 1);
}
