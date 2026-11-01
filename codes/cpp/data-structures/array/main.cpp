#include <iostream>

using namespace std;

int a[5];

int main() {
    int i;

    for (i = 0; i < 5; ++i) {
        cin >> a[i];
    }

    // 첫 번째와 세 번째 원소 조회
    cout << a[0] << '\n';
    cout << a[2] << '\n';

    a[2] = 9; // 세 번째 원소 갱신

    cout << a[2] << '\n';
}
