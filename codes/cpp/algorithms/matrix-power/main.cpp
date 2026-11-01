#include <iostream>
#include <vector>

using namespace std;

int n;
vector<vector<int>> a, t;

vector<vector<int>> mul(const vector<vector<int>>& a, const vector<vector<int>>& b) {
    int i, j, k;
    vector<vector<int>> c(n, vector<int>(n));

    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            for (k = 0; k < n; ++k) {
                // a의 i행과 b의 j열에서 같은 위치의 곱을 누적
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return c;
}

vector<vector<int>> power(const vector<vector<int>>& a, int b) {
    int i;
    vector<vector<int>> t;

    // 행렬의 0제곱은 대각 원소가 1인 항등행렬
    if (b == 0) {
        t.assign(n, vector<int>(n));
        for (i = 0; i < n; ++i) {
            t[i][i] = 1;
        }
        return t;
    }
    // 절반 지수의 결과를 한 번 계산하여 재사용
    t = power(a, b / 2);
    t = mul(t, t);
    // 홀수 지수에서 제곱 후 남은 행렬 a를 한 번 곱함
    if (b % 2 == 1) t = mul(t, a);
    return t;
}

int main() {
    int b, i, j;

    cin >> n >> b;
    a.assign(n, vector<int>(n));
    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            cin >> a[i][j];
        }
    }
    // 절반 지수의 결과를 한 번 계산하여 재사용
    t = power(a, b);

    for (const auto& row : t) {
        for (int x : row) {
            cout << x << ' ';
        }
        cout << '\n';
    }
}
