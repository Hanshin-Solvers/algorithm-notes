#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int main() {
    int n, k, i, l, r, m, cnt, ans;

    cin >> n >> k;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }
    l = 1;
    r = *max_element(v.begin(), v.end());
    ans = 0;
    while (l <= r) {
        m = (l + r) / 2;
        cnt = 0;
        for (int x : v) {
            cnt += x / m;
        }
        // 필요한 조각 수를 만들 수 있으면 답을 저장하고 더 긴 길이 탐색
        if (cnt >= k) {
            ans = m;
            l = m + 1;
        }
        // 조각 수가 부족하면 길이를 줄여 다시 탐색
        else r = m - 1;
    }
    cout << ans << '\n';
}
