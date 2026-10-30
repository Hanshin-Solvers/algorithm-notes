#include <iostream>
#include <set>

using namespace std;

int main() {
    int n, i, x;
    set<int> st;
    bool ok;

    cin >> n;

    for (i = 0; i < n; ++i) {
        cin >> x;
        st.insert(x); // 중복 값은 한 번만 저장
    }

    cout << st.size() << '\n';
    ok = true;
    // 정렬 집합의 원소를 오름차순으로 출력
    for (int v : st) {
        if (!ok) cout << ' ';

        cout << v;
        ok = false;
    }

    cout << '\n';
}
