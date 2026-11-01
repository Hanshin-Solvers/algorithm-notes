#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct point {
    int x, y;
};

bool compare(const point& a, const point& b) {
    if (a.x != b.x) return a.x < b.x;
    return a.y < b.y;
}

bool same(const point& a, const point& b) {
    return a.x == b.x && a.y == b.y;
}

// 세 점의 방향 판별: 양수는 반시계, 0은 일직선, 음수는 시계 방향
int cross(const point& a, const point& b, const point& c) {
    return (b.x - a.x) * (c.y - a.y)
         - (b.y - a.y) * (c.x - a.x);
}

vector<point> v, lo, hi, ans;

int main() {
    int n;

    cin >> n;
    v.resize(n);
    for (point& p : v) {
        cin >> p.x >> p.y;
    }

    // x좌표 우선, 같으면 y좌표 순으로 정렬하여 경계 탐색 순서 결정
    sort(v.begin(), v.end(), compare);
    // 같은 좌표의 점을 하나로 합침
    v.erase(unique(v.begin(), v.end(), same), v.end());

    if (v.size() == 1) ans = v;
    else {
        // 아래쪽 경계 구성
        for (const point& p : v) {
            // 시계 방향 또는 일직선인 마지막 점을 제거하여 반시계 방향 유지
            while (lo.size() >= 2 && cross(lo[lo.size() - 2], lo.back(), p) <= 0) {
                lo.pop_back();
            }
            lo.push_back(p);
        }
        reverse(v.begin(), v.end());
        // 위쪽 경계 구성
        for (const point& p : v) {
            // 시계 방향 또는 일직선인 마지막 점을 제거하여 반시계 방향 유지
            while (hi.size() >= 2 && cross(hi[hi.size() - 2], hi.back(), p) <= 0) {
                hi.pop_back();
            }
            hi.push_back(p);
        }
        // 위아래 경계에 중복되는 양 끝점 제외
        lo.pop_back();
        hi.pop_back();
        ans = lo;
        ans.insert(ans.end(), hi.begin(), hi.end());
    }

    cout << ans.size() << '\n';
    for (const point& p : ans) {
        cout << p.x << ' ' << p.y << '\n';
    }
}
