#include <bits/stdc++.h>

using namespace std;

int main() {
    int b, c, x, d;
    string s, out, digit = "0123456789ABCDEF";

    cin >> b >> c >> s;
    x = 0;
    for (char ch : s) {
        d = digit.find(ch);
        x = x * b + d;
    }

    out = "";
    do {
        out += digit[x % c];
        x /= c;
    } while (x > 0);
    reverse(out.begin(), out.end());
    cout << out << '\n';
}
