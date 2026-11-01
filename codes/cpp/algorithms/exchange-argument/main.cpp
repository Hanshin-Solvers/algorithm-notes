#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(int a, int b) {
    // 처리 시간 오름차순
    return a < b;
}

vector<int> v;

int main() {
    int n, i, sum, ans;

    cin >> n;
    v.resize(n);
    for (i = 0; i < n; ++i) {
        cin >> v[i];
    }

    sort(v.begin(), v.end(), compare);
    sum = 0;
    ans = 0;
    for (int x : v) {
        // 현재 작업의 완료 시각과 전체 합 갱신
        sum += x;
        ans += sum;
    }

    cout << ans << '\n';
}
