---
title: 문자열 기본 조작
description: 문자열 기본 조작의 개념과 사용법을 다룹니다.
topic: string-operations
---

## 개념

### 부분 문자열 추출

문자열에서 필요한 구간을 잘라 새로운 문자열을 만듭니다. `abcdef`의 위치 $1$부터 $4$ 직전까지 추출하면 `bcd`입니다.

| 동작 | C++ | Java | Python |
| --- | --- | --- | --- |
| 길이 | `s.size()` | `s.length()` | `len(s)` |
| 한 문자 접근 | `s[i]` | `s.charAt(i)` | `s[i]` |
| 구간 [l, r) 추출 | `s.substr(l, r - l)` | `s.substring(l, r)` | `s[l:r]` |
| 문자열 결합 | `s + t` | `s + t` | `s + t` |

C++ `substr`의 두 번째 인자는 길이입니다. Java `substring`의 두 번째 인자와 Python 슬라이스의 끝 인덱스는 포함하지 않는 끝 위치입니다.

### 기본 검색

문자열 안에 다른 문자열이 처음 등장하는 위치를 찾습니다. 시작 위치를 함께 지정하면 그 위치부터 검색합니다.

| 동작 | C++ | Java | Python |
| --- | --- | --- | --- |
| 처음 등장하는 위치 | `s.find(t)` | `s.indexOf(t)` | `s.find(t)` |
| p부터 검색 | `s.find(t, p)` | `s.indexOf(t, p)` | `s.find(t, p)` |
| 찾지 못한 결과 | `string::npos` | `-1` | `-1` |

C++의 검색 결과는 `string::npos`와 비교한 뒤 인덱스로 사용합니다. 검색의 알고리즘 원리는 [Naive Pattern Search](/algorithm-notes/notes/algorithms/pattern-search/)와 [KMP](/algorithm-notes/notes/algorithms/kmp/)에서 다룹니다.

### 분리·결합·치환

문자열을 구분자로 나누거나, 여러 문자열 사이에 구분자를 넣어 합칠 수 있습니다.

| 동작 | C++ | Java | Python |
| --- | --- | --- | --- |
| 공백으로 단어 분리 | `istringstream`에서 `>>` 반복 | `StringTokenizer` | `s.split()` |
| 쉼표로 분리 | `getline(ss, t, ',')` 반복 | `s.split(",", -1)` | `s.split(',')` |
| 단어 사이 공백으로 결합 | 반복하며 구분자와 단어 추가 | `String.join(" ", lst)` | `' '.join(lst)` |
| 위치 p부터 k개 문자 교체 | `s.replace(p, k, t)` | 앞부분 + t + 뒷부분 | `s[:p] + t + s[p+k:]` |
| 문자열의 모든 일치 부분 치환 | 검색 위치를 갱신하며 교체 | `s.replace(old, next)` | `s.replace(old, new)` |

Java의 `split`은 구분자를 정규식으로 해석합니다. 점처럼 정규식에서 특별한 의미가 있는 문자를 구분자로 쓸 때는 이스케이프가 필요합니다. `-1`은 맨 끝의 빈 항목도 보존합니다. C++에서 `getline`을 반복하는 방식은 맨 끝 구분자 뒤의 빈 항목을 별도로 처리해야 합니다.

Java와 Python의 문자열은 변경 연산의 결과로 새 문자열을 만듭니다. 많은 조각을 결합할 때는 Java의 `StringBuilder`, Python의 `join`으로 모아서 처리합니다.

### 복잡도

문자열 길이를 $N$, 추출 길이를 $K$, 결합 결과 길이를 $L$이라고 합니다. 아래 표는 영문 문자열을 기준으로 합니다.

| 연산 | 시간복잡도 | 공간복잡도 |
| --- | --- | --- |
| 부분 문자열 생성 | $O(K)$ | 결과 $O(K)$ |
| 한 구분자로 분리 | $O(N)$ | 결과 $O(N)$ |
| 모아 둔 조각 결합 | $O(L)$ | 결과 $O(L)$ |

## 예제

### 문제

문자열에서 L번째 문자부터 R번째 문자까지 추출합니다.

### 입력

첫째 줄에 길이가 $1$ 이상 $100$ 이하인 영어 소문자 문자열이 주어집니다. 둘째 줄에 $L,R$이 공백으로 구분되어 주어집니다. $1 \le L \le R \le \text{문자열 길이}$입니다.

### 출력

추출한 문자열을 출력합니다.
