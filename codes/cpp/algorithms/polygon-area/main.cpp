#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

struct point {
    int x, y;
};

vector<point> v;

int main() {
    int n, i, j, area;

    cin >> n;
    v.resize(n);
    for (point& p : v) {
        cin >> p.x >> p.y;
    }

    area = 0;
    for (i = 0; i < n; ++i) {
        // 마지막 꼭짓점 다음은 첫 꼭짓점으로 연결
        j = (i + 1) % n;
        // 인접한 두 꼭짓점의 외적을 부호 그대로 누적
        area += v[i].x * v[j].y - v[i].y * v[j].x;
    }
    // 합을 구한 뒤 절댓값을 취하여 넓이의 두 배 계산
    area = abs(area);

    cout << area / 2;
    if (area % 2 == 0) cout << ".0\n";
    else cout << ".5\n";
}
