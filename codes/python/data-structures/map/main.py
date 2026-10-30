n = int(input())
cnt = {}

for _ in range(n):
    s = input().strip()
    # 처음 등장한 단어는 0부터 횟수 증가
    cnt[s] = cnt.get(s, 0) + 1

# 단어를 기준으로 키와 값의 쌍을 정렬하여 출력
for k, v in sorted(cnt.items()):
    print(k, v)
