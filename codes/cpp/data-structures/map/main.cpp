#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    int n, i;
    map<string, int> cnt;
    string s;

    cin >> n;

    for (i = 0; i < n; ++i) {
        cin >> s;
        ++cnt[s]; // 처음 등장한 단어는 0부터 횟수 증가
    }

    // 정렬 맵의 키 순서대로 단어와 횟수 출력
    for (const auto& [k, v] : cnt) {
        cout << k << ' ' << v << '\n';
    }
}
