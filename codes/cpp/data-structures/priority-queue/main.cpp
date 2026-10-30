#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

int main() {
    int n, i, x;
    priority_queue<int, vector<int>, greater<int>> pq;
    bool ok;

    cin >> n;
    for (i = 0; i < n; ++i) {
        cin >> x;

        pq.push(x);
    }
    ok = true;
    while (!pq.empty()) {
        if (!ok) cout << ' ';

        cout << pq.top();
        pq.pop();
        ok = false;
    }

    cout << '\n';
}
