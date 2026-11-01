---
title: 정렬 함수와 사용자 정의 정렬
description: 세 언어의 정렬 함수, 비교 기준, 안정 정렬과 불안정 정렬을 설명합니다.
topic: sorting
---

## 개념

정렬은 비교 기준에 따라 원소의 순서를 정하는 작업입니다. $[3,1,2]$를 작은 수부터 나열하면 $[1,2,3]$이 되고, 큰 수부터 나열하면 $[3,2,1]$이 됩니다. 각각 오름차순과 내림차순입니다.

### 정렬 대상과 함수

아래에서는 세 언어 모두 정수 목록을 정렬합니다. Java는 사용자 정의 비교까지 같은 형식으로 설명하기 위해 `Integer[]`를 사용합니다.

| 항목 | C++ | Java | Python |
| --- | --- | --- | --- |
| 정렬 대상 | `vector<int> v` | `Integer[] a` | 정수 리스트 `lst` |
| 필요한 라이브러리 | `<algorithm>`, `<vector>` | `java.util.Arrays`, `java.util.Comparator` | 내장 함수 사용 |
| 원본 정렬 | `sort(v.begin(), v.end(), compare)` | `Arrays.sort(a, cmp)` | `lst.sort()` |
| 비교 기준 전달 | `bool compare` 함수 | `Comparator<Integer> cmp` | `key`와 `reverse` 인자 |

세 함수 모두 원본의 순서를 바꿉니다. `compare`와 `cmp`에는 아래에서 정하는 비교 기준을 넣습니다. Java의 `int[]`는 `Arrays.sort(a)`로 오름차순 정렬하며, Comparator를 전달하려면 `Integer[]`처럼 객체를 원소로 갖는 배열을 사용합니다.

### 오름차순과 내림차순

두 원소의 앞뒤 순서를 정하는 방식을 먼저 확인합니다.

| 항목 | C++ | Java | Python |
| --- | --- | --- | --- |
| 기준의 의미 | `compare(x, y)`가 참이면 `x`가 먼저 옴 | `cmp.compare(x, y)`가 음수이면 `x`가 먼저 옴 | `key`로 얻은 값이 작은 원소가 먼저 옴 |
| 오름차순 기준 | `bool compare(int x, int y)`에서 `return x < y;` | `Comparator<Integer> cmp = (x, y) -> Integer.compare(x, y);` | 기본 기준으로 값 자체를 비교 |
| 오름차순 호출 | `sort(v.begin(), v.end(), compare)` | `Arrays.sort(a, cmp)` | `lst.sort()` |
| 내림차순 기준 | `bool compare(int x, int y)`에서 `return x > y;` | `Comparator<Integer> cmp = (x, y) -> Integer.compare(y, x);` | `reverse=True`로 순서를 뒤집음 |
| 내림차순 호출 | `sort(v.begin(), v.end(), compare)` | `Arrays.sort(a, cmp)` | `lst.sort(reverse=True)` |

C++과 Java는 원하는 방향에 맞게 비교 함수의 내용을 정합니다. Java의 비교 결과는 앞에 올 때 음수, 같은 기준일 때 $0$, 뒤에 올 때 양수입니다. Python의 `key`는 각 원소에서 비교할 값을 꺼내는 함수입니다.

### 부분 구간과 복사본 정렬

구간 $[l,r)$은 인덱스 $l$부터 $r-1$까지입니다. 예를 들어 $[8,3,1,2,9]$에서 $[1,4)$만 오름차순으로 정렬하면 $[8,1,2,3,9]$가 됩니다. 아래의 `compare`와 `cmp`는 오름차순 기준입니다.

| 동작 | C++ | Java | Python |
| --- | --- | --- | --- |
| 부분 구간 정렬 | `sort(v.begin() + l, v.begin() + r, compare)` | `Arrays.sort(a, l, r, cmp)` | `lst[l:r] = sorted(lst[l:r])` |
| 복사본 만들기 | `w = v` | `b = a.clone()` | `out = sorted(lst)` |
| 복사본 정렬 | `sort(w.begin(), w.end(), compare)` | `Arrays.sort(b, cmp)` | 앞의 `sorted`가 정렬된 복사본을 반환 |

`w`는 `vector<int>`, `b`는 `Integer[]`로 선언한 변수입니다. Python의 `lst.sort()`는 원본을 정렬하고 `None`을 반환하며, `sorted(lst)`는 새 리스트를 반환합니다.

### 여러 기준으로 정렬

참가자를 `(번호, 점수)`로 저장하고, 점수 내림차순·번호 오름차순으로 정렬하겠습니다. 입력이 $(2,90),(3,80),(1,90)$이면 결과는 $(1,90),(2,90),(3,80)$입니다. 먼저 점수를 비교하고, 점수가 같을 때 번호를 비교합니다.

| 항목 | C++ | Java | Python |
| --- | --- | --- | --- |
| 참가자 한 명 | `pair<int, int>` | 길이 $2$인 `int[]` | `(번호, 점수)` 튜플 |
| 번호·점수 접근 | `x.first`, `x.second` | `x[0]`, `x[1]` | `x[0]`, `x[1]` |
| 점수가 다를 때 | `compare`에서 `x.second > y.second` 반환 | Comparator에서 `Integer.compare(y[1], x[1])` 반환 | 키의 첫 값 `-x[1]` 비교 |
| 점수가 같을 때 | `compare`에서 `x.first < y.first` 반환 | Comparator에서 `Integer.compare(x[0], y[0])` 반환 | 키의 다음 값 `x[0]` 비교 |
| 정렬 호출 | `sort(v.begin(), v.end(), compare)` | `Arrays.sort(a, cmp)` | `lst.sort(key=lambda x: (-x[1], x[0]))` |

이 경우 C++의 비교 함수는 두 `pair<int, int>`를 받고, Java의 `cmp`는 두 `int[]`를 비교하는 `Comparator<int[]>`입니다. Java의 정렬 대상은 참가자들을 담은 `int[][]`이며, 각 원소가 배열 객체이므로 Comparator를 사용할 수 있습니다.

Python은 튜플의 첫 값부터 비교하고, 같으면 다음 값을 비교합니다. 점수에 음수를 붙이면 $90$점의 키 $-90$이 $80$점의 키 $-80$보다 작으므로 높은 점수가 먼저 옵니다.

### 비교 기준의 일관성

같은 원소를 비교할 때와 비교 방향을 바꿀 때도 기준이 일관되어야 합니다.

| 항목 | C++ | Java | Python |
| --- | --- | --- | --- |
| 모든 비교 항목이 같음 | 양방향 모두 `false` | 양방향 모두 $0$ | 같은 키를 반환 |
| 순서 관계 | `x`가 `y`보다 앞이면 역방향은 `false` | 비교 방향을 바꾸면 결과의 부호도 반대 | 정한 키의 순서에 따라 비교 |
| 작성 시 확인 | `<`, `>`로 비교하고 `<=`, `>=`를 사용하지 않음 | 정수는 뺄셈 대신 `Integer.compare`로 비교 | 같은 원소에서 항상 같은 키를 계산 |

세 원소의 순서도 이어져야 합니다. `x`가 `y`보다 앞이고 `y`가 `z`보다 앞이면 `x`가 `z`보다 앞이어야 합니다. Java에서 두 정수를 빼서 비교하면 뺄셈 결과가 자료형 범위를 벗어날 수 있으므로 `Integer.compare`를 사용합니다.

### 안정 정렬과 불안정 정렬

안정 정렬(stable sort)은 정렬 기준이 같은 원소들의 입력 순서를 유지합니다. 불안정 정렬(unstable sort)은 그 순서의 유지를 보장하지 않습니다. 둘 다 정렬 기준에 맞게 원소를 나열하며, 차이는 동점 원소의 상대적인 순서입니다.

참가자가 $(2,90),(3,80),(1,90)$ 순서로 입력되었고, 이번에는 점수 내림차순만 기준으로 사용한다고 하겠습니다. $90$점인 두 참가자 중에서는 $2$번이 먼저 입력되었습니다.

| 정렬 방법 | 가능한 결과 | 동점 처리 |
| --- | --- | --- |
| 안정 정렬 | $(2,90),(1,90),(3,80)$ | $2$번이 $1$번보다 앞에 온 입력 순서를 유지 |
| 불안정 정렬 | $(2,90),(1,90),(3,80)$ 또는 $(1,90),(2,90),(3,80)$ | 두 $90$점 참가자의 순서를 보장하지 않음 |

불안정 정렬이라고 해서 동점자의 순서가 반드시 바뀌는 것은 아닙니다. 위 표의 두 결과가 모두 허용되므로, 입력 순서가 필요할 때는 안정 정렬을 선택합니다.

| 항목 | C++ | Java | Python |
| --- | --- | --- | --- |
| 안정 정렬 함수 | `stable_sort(v.begin(), v.end(), compare)` | 객체 배열의 `Arrays.sort(a, cmp)`, 리스트의 `lst.sort(cmp)` | `lst.sort(...)`, `sorted(lst, ...)` |
| 안정성을 보장하지 않는 함수 | `sort(v.begin(), v.end(), compare)` | 기본형 배열의 `Arrays.sort(a)` | 여기서 사용하는 두 함수는 안정 정렬 |
| 점수만 비교 | `compare`에서 `x.second > y.second` 반환 | `cmp`에서 `Integer.compare(y[1], x[1])` 반환 | `key=lambda x: -x[1]` |

Java의 기본형 정수 배열에서는 같은 값의 원소를 값만으로 구분할 수 없습니다. 번호와 점수를 함께 저장한 참가자처럼 동점 원소를 구분해야 할 때 안정성의 차이가 드러납니다. 언어별 보장 사항은 [C++ 정렬 명세](https://eel.is/c++draft/alg.sort), [Java Arrays 문서](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Arrays.html), [Python 정렬 문서](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts)에서 확인할 수 있습니다.

점수 내림차순에 번호 오름차순을 추가하면 $1$번이 $2$번보다 먼저 옵니다. 이는 번호를 비교해 정한 순서입니다. 안정 정렬은 지정한 비교 항목이 모두 같을 때 입력 순서를 유지하므로, 동점자에게 별도의 순서를 요구하는 문제에서는 그 항목을 비교 기준에 추가합니다.

### 복잡도

원소 수를 $N$이라고 하며, 정수나 길이가 고정된 키를 비교하는 경우입니다. 추가 공간에는 정렬 대상 자체의 저장 공간을 포함하지 않습니다.

| 항목 | C++ | Java | Python |
| --- | --- | --- | --- |
| 시간복잡도 | `sort`: $O(N\log N)$ | 객체 배열 정렬: $O(N\log N)$ | `sort`, `sorted`: 최악 $O(N\log N)$ |
| 추가 공간 | `sort`: 일반적인 구현에서 $O(\log N)$ | 객체 배열 정렬: $O(N)$ | 정렬 작업: $O(N)$ |
| 정렬된 복사본 저장 | $O(N)$ | $O(N)$ | $O(N)$ |

C++20의 `stable_sort`는 충분한 추가 메모리를 확보하면 $O(N\log N)$번 비교하며, 확보하지 못하면 $O(N\log^2 N)$번 비교할 수 있습니다. 일반적인 구현은 병합에 사용할 $O(N)$ 크기의 임시 공간을 사용합니다.

## 예제

### 문제

참가자를 점수가 높은 순서로 나열한다. 점수가 같으면 번호가 작은 참가자가 먼저 온다.

### 입력

첫째 줄에 참가자 수 $N$이 주어진다. $1\le N\le100$이다.

다음 $N$개 줄에 참가자의 번호 $a$와 점수 $s$가 공백을 사이에 두고 주어진다. $1\le a<10\,000$; $1\le s\le100$이다. 참가자 번호는 서로 다르다.

### 출력

정렬된 참가자 번호를 한 줄에 공백으로 구분하여 출력한다.
