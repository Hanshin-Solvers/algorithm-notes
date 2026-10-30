#include <bits/stdc++.h>

using namespace std;

int main() {
    const bool DEBUG = false;
    int n, sum;
    vector<int> v;
    chrono::steady_clock::time_point start, finish;
    double ms;

    cin >> n;
    v.resize(n);
    for (int& x : v) {
        cin >> x;
    }

    start = chrono::steady_clock::now();
    sum = 0;
    for (int x : v) {
        sum += x;
    }
    finish = chrono::steady_clock::now();
    ms = chrono::duration<double, milli>(finish - start).count();

    // DEBUG가 true이면 표준 오류에 기록
    if (DEBUG) {
        cerr << "sum=" << sum << '\n';
        cerr << "elapsed_ms=" << ms << '\n';
    }
    cout << sum << '\n';
}
