#include <iostream>

using namespace std;

int main() {
    int a, b;
    long long area;

    cin >> a >> b;

    // 곱셈 전에 long long으로 확장
    area = 1LL * a * b;

    cout << area << '\n';
}
