#include <iostream>
#include <unordered_map>
#include <cstddef>

using namespace std;

struct Key {
    int x, y;

    bool operator==(const Key& a) const {
        // 두 좌표가 모두 같으면 같은 키
        return x == a.x && y == a.y;
    }
};

struct Hash {
    size_t operator()(const Key& a) const {
        // 0 이상 1000 미만인 두 좌표를 하나의 값으로 변환
        return static_cast<size_t>(a.x) * 1000 + a.y;
    }
};

int main() {
    int n, q, i;
    Key a;
    unordered_map<Key, int, Hash> cnt;
    unordered_map<Key, int, Hash>::iterator it;

    cin >> n >> q;
    cnt.reserve(n);
    for (i = 0; i < n; ++i) {
        cin >> a.x >> a.y;
        ++cnt[a];
    }

    for (i = 0; i < q; ++i) {
        cin >> a.x >> a.y;
        // 없는 키를 추가하지 않고 조회
        it = cnt.find(a);
        if (it != cnt.end()) cout << it->second << '\n';
        else cout << 0 << '\n';
    }
}
