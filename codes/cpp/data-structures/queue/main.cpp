#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main() {
    int n, i, x;
    queue<int> q;
    string op;

    cin >> n;

    for (i = 0; i < n; ++i) {
        cin >> op;

        if (op == "push") {
            cin >> x;

            q.push(x);
        }
        else if (op == "size") cout << q.size() << '\n';
        else if (q.empty()) cout << "EMPTY\n";
        else if (op == "front") cout << q.front() << '\n';
        else {
            cout << q.front() << '\n';
            q.pop();
        }
    }
}
