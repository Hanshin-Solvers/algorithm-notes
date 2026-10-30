#include <bits/stdc++.h>

using namespace std;

int main() {
    string s, p;
    int n, m, i, j;
    vector<int> pi, ans;

    cin >> s >> p;
    n = (int)s.size();
    m = (int)p.size();
    pi.assign(m, 0);

    // 패턴의 접두사 함수 계산
    j = 0;
    for (i = 1; i < m; ++i) {
        while (j > 0 && p[i] != p[j]) {
            j = pi[j - 1];
        }
        if (p[i] == p[j]) ++j;
        pi[i] = j;
    }

    // 본문 탐색과 겹치는 일치 처리
    j = 0;
    for (i = 0; i < n; ++i) {
        while (j > 0 && s[i] != p[j]) {
            j = pi[j - 1];
        }
        if (s[i] == p[j]) ++j;
        if (j == m) {
            ans.push_back(i - m + 1);
            j = pi[j - 1];
        }
    }

    cout << ans.size() << '\n';
    for (int x : ans) {
        cout << x << ' ';
    }
    cout << '\n';
}
