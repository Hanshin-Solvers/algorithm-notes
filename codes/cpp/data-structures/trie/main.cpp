#include <iostream>
#include <string>

using namespace std;

// 최대 100개 단어 × 길이 20 + 루트
int t[2001][26], sz;
bool fin[2001];

void add(const string& s) {
    int u, x;

    u = 0;
    for (char c : s) {
        x = c - 'a';
        // 해당 문자로 이어지는 노드가 없으면 새 노드 생성
        if (t[u][x] == 0) t[u][x] = ++sz;
        u = t[u][x];
    }
    // 접두사 경로와 완성된 단어를 구분하는 끝 표시
    fin[u] = true;
}

int find(const string& s) {
    int u, x;

    u = 0;
    for (char c : s) {
        x = c - 'a';
        // 해당 접두사 경로가 없으므로 검색 종료
        if (t[u][x] == 0) return -1;
        u = t[u][x];
    }
    return u;
}

int main() {
    int n, q, i, u;
    string s, op;
    bool ok;

    cin >> n >> q;
    for (i = 0; i < n; ++i) {
        cin >> s;
        add(s);
    }

    for (i = 0; i < q; ++i) {
        cin >> op >> s;
        u = find(s);

        // 단어 검색은 끝 표시까지 확인
        if (op == "word") ok = u != -1 && fin[u];
        else ok = u != -1;

        if (ok) cout << "YES\n";
        else cout << "NO\n";
    }
}
