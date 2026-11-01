#include <iostream>
#include <string>

using namespace std;

int main() {
    string s, t;
    int l, r;

    cin >> s >> l >> r;

    // 시작 위치와 추출 길이
    t = s.substr(l - 1, r - l + 1);

    cout << t << '\n';
}
