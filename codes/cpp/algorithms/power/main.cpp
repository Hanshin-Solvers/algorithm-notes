#include <bits/stdc++.h>

using namespace std;

int power(int a, int b) {
    int x;

    if (b == 0) return 1;
    x = power(a, b / 2);
    x *= x;
    if (b % 2 == 1) x *= a;
    return x;
}

int main() {
    int a, b;

    cin >> a >> b;
    cout << power(a, b) << '\n';
}
