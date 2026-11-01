#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main() {
    int a, b, c, n, up, down, near;
    double x;

    cin >> a >> b >> c >> n;

    // 소수 부분까지 계산하도록 실수로 평균 계산
    x = (a + b + c) / 3.0;
    up = (int)ceil(x);
    down = (int)floor(x);
    near = (int)round(x);

    // 소수점 아래 n자리를 고정하고 부족한 자리는 0으로 채움
    cout << fixed << setprecision(n) << x << '\n';
    cout << up << ' ' << down << ' ' << near << '\n';
}
