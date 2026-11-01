#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> pi, ans;

int main() {
    string s, p;
    int n, m, i, j;

    cin >> s >> p;
    n = (int)s.size();
    m = (int)p.size();
    pi.assign(m, 0);

    // 패턴의 접두사 함수 계산
    j = 0;
    for (i = 1; i < m; ++i) {
        // 불일치 시 이미 일치한 부분의 접두사·접미사를 이용해 다음 후보 길이로 이동
        while (j > 0 && p[i] != p[j]) {
            j = pi[j - 1];
        }
        if (p[i] == p[j]) ++j;
        // pi[i]: 패턴의 0~i 구간에서 자신을 제외한 최장 공통 접두사·접미사 길이
        pi[i] = j;
    }

    // 본문 탐색과 겹치는 일치 처리
    j = 0;
    for (i = 0; i < n; ++i) {
        // 불일치 시 이미 일치한 부분의 접두사·접미사를 이용해 다음 후보 길이로 이동
        while (j > 0 && s[i] != p[j]) {
            j = pi[j - 1];
        }
        if (s[i] == p[j]) ++j;
        // 패턴 전체 일치: 시작 위치 기록 후 겹치는 다음 일치를 위해 j 복구
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
