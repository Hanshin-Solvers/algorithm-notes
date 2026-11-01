#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> v;

int main() {
    int q, i, x, j;
    string op;

    cin >> q;

    for (i = 0; i < q; ++i) {
        cin >> op;

        if (op == "append") {
            cin >> x;

            v.push_back(x);
        }
        else if (op == "pop") {
            if (v.empty()) cout << "EMPTY\n";
            else {
                cout << v.back() << '\n';
                v.pop_back();
            }
        }
        else if (op == "get") {
            cin >> j;
            cout << v.at(j) << '\n';
        }
        else cout << v.size() << '\n';
    }
}
