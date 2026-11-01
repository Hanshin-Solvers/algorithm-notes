#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int main() {
    int n, i;

    cin >> n;
    for (i = 1; i <= n / i; ++i) {
        if (n % i == 0) {
            v.push_back(i);
            if (i != n / i) v.push_back(n / i);
        }
    }
    sort(v.begin(), v.end());

    for (int x : v) {
        cout << x << ' ';
    }
    cout << '\n';
}
