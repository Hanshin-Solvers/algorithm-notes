#include <bits/stdc++.h>

using namespace std;

int main() {
    string s, out;
    int n, sum;

    cin >> s;
    n = stoi(s);
    sum = 0;

    for (char c : s) {
        sum += c - '0';
    }
    // 정수를 문자열로 변환
    out = to_string(n);

    cout << out << '\n' << sum << '\n';
}
