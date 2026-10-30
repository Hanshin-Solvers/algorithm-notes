#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b, q, r, up;

    cin >> a >> b;
    q = a / b;
    r = a % b;

    // 음수 나머지를 내림 나눗셈의 나머지로 보정
    if (r < 0) {
        --q;
        r += b;
    }
    up = q;
    if (r > 0) ++up;

    cout << q << ' ' << up << ' ' << r << '\n';
}
