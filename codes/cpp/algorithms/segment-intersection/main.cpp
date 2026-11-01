#include <iostream>
#include <algorithm>

using namespace std;

struct point {
    int x, y;
};

// 세 점의 외적으로 기준 직선에 대한 방향 계산
int cross(const point& a, const point& b, const point& c) {
    return (b.x - a.x) * (c.y - a.y)
         - (b.y - a.y) * (c.x - a.x);
}

int sign(int x) {
    if (x > 0) return 1;
    else if (x == 0) return 0;
    else return -1;
}

bool overlap(int a, int b, int c, int d) {
    return max(min(a, b), min(c, d)) <= min(max(a, b), max(c, d));
}

int main() {
    point a, b, c, d;
    int x, y, z, w;
    bool ok;

    cin >> a.x >> a.y >> b.x >> b.y;
    cin >> c.x >> c.y >> d.x >> d.y;
    // 외적을 -1, 0, 1로 바꾸어 양쪽 선분의 방향 조건 비교
    x = sign(cross(a, b, c));
    y = sign(cross(a, b, d));
    z = sign(cross(c, d, a));
    w = sign(cross(c, d, b));

    // 네 점이 일직선이면 x좌표와 y좌표의 공통 구간 확인
    if (x == 0 && y == 0 && z == 0 && w == 0) {
        ok = overlap(a.x, b.x, c.x, d.x)
          && overlap(a.y, b.y, c.y, d.y);
    }
    // 각 직선의 양쪽에 상대 선분의 끝점이 놓이는지 확인
    else ok = (x * y <= 0 && z * w <= 0);

    cout << (ok ? "YES" : "NO") << '\n';
}
