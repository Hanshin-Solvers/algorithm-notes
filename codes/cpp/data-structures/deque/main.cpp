#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
    int q, i, x;
    deque<int> dq;
    string op;

    cin >> q;

    for (i = 0; i < q; ++i) {
        cin >> op;

        if (op == "push_front") {
            cin >> x;

            dq.push_front(x);
        }
        else if (op == "push_back") {
            cin >> x;

            dq.push_back(x);
        }
        else if (op == "size") cout << dq.size() << '\n';
        else if (dq.empty()) cout << "EMPTY\n";
        else if (op == "front") cout << dq.front() << '\n';
        else if (op == "back") cout << dq.back() << '\n';
        else if (op == "pop_front") {
            cout << dq.front() << '\n';
            dq.pop_front();
        }
        else {
            cout << dq.back() << '\n';
            dq.pop_back();
        }
    }
}
