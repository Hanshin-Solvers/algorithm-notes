#include <iostream>

using namespace std;

int main() {
    int a, m, r;

    cin >> a >> m;

    // 나머지를 0 이상 m 미만으로 보정
    r = a % m;
    if (r < 0) r += m;

    cout << r << '\n';
}
