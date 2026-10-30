#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, k, x;
    vector<int> v, w;

    cin >> n;
    v.resize(n);
    for (int& a : v) {
        cin >> a;
    }
    cin >> k >> x;

    // 원소를 복사한 뒤 복사본 수정
    w = v;
    w[k - 1] = x;

    for (int a : v) {
        cout << a << ' ';
    }
    cout << '\n';
    for (int a : w) {
        cout << a << ' ';
    }
    cout << '\n';
}
