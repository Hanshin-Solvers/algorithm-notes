#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// t[k]: 길이 k+1 수열의 최소 끝값, pos[k]: 해당 원소 위치, p[i]: 이전 원소 위치
vector<int> v, t, pos, p, ans;

int main() {
    int n, i, k;

    cin >> n;
    v.resize(n);
    p.assign(n, -1);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }

    for (i = 0; i < n; ++i) {
        // 현재 값 이상인 첫 위치를 찾아 같은 값으로 수열 길이가 늘어나는 것을 방지함
        k = lower_bound(t.begin(), t.end(), v[i]) - t.begin();

        // 후보 교체 전에 이전 원소의 위치 저장
        if (k > 0) p[i] = pos[k - 1];
        if (k == (int)t.size()) {
            t.push_back(v[i]);
            pos.push_back(i);
        }
        else {
            t[k] = v[i];
            pos[k] = i;
        }
    }

    // 가장 긴 수열의 끝에서 이전 위치를 따라 복원
    i = pos.back();
    while (i != -1) {
        ans.push_back(v[i]);
        i = p[i];
    }
    reverse(ans.begin(), ans.end());

    cout << ans.size() << '\n';
    for (int x : ans) {
        cout << x << ' ';
    }
    cout << '\n';
}
