#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    string s, ans;
    int n, x, r;

    cin >> s >> n;
    x = 0;

    // 왼쪽부터 26진수의 자릿값을 누적함
    for (char c : s) {
        x = x * 26 + (c - 'a');
    }
    cout << x << '\n';

    // 낮은 자리부터 구한 뒤 순서를 뒤집음
    if (n == 0) ans = "a";
    while (n > 0) {
        r = n % 26;
        ans += char('a' + r);
        n /= 26;
    }
    reverse(ans.begin(), ans.end());
    cout << ans << '\n';
}
