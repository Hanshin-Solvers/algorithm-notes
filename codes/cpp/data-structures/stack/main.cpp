#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    int q, i, x;
    stack<int> st;
    string op;

    cin >> q;

    for (i = 0; i < q; ++i) {
        cin >> op;

        if (op == "push") {
            cin >> x;

            st.push(x);
        }
        else if (op == "size") cout << st.size() << '\n';
        else if (st.empty()) cout << "EMPTY\n";
        else if (op == "top") cout << st.top() << '\n';
        else {
            cout << st.top() << '\n';
            st.pop();
        }
    }
}
