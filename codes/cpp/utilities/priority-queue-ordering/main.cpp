#include <iostream>
#include <queue>

using namespace std;

struct Job {
    int id, p;

    bool operator<(const Job& a) const {
        // 우선순위 값이 크면 나중에 처리
        if (p != a.p) return p > a.p;
        // 같은 우선순위이면 번호가 큰 작업을 나중에 처리
        return id > a.id;
    }
};

int main() {
    int n, i;
    Job a;
    priority_queue<Job> pq;

    cin >> n;
    for (i = 0; i < n; ++i) {
        cin >> a.id >> a.p;
        pq.push(a);
    }

    while (!pq.empty()) {
        // 값을 복사한 뒤 큐에서 제거
        a = pq.top();
        pq.pop();
        cout << a.id << ' ';
    }
    cout << '\n';
}
