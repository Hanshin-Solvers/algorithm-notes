import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        String s, p;
        int n, m, i, j;
        int[] pi;
        ArrayList<Integer> ans;

        sc = new Scanner(System.in);
        s = sc.next();
        p = sc.next();
        n = s.length();
        m = p.length();
        pi = new int[m];
        ans = new ArrayList<>();

        // 패턴의 접두사 함수 계산
        j = 0;
        for (i = 1; i < m; ++i) {
            // 불일치 시 이미 일치한 부분의 접두사·접미사를 이용해 다음 후보 길이로 이동
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (p.charAt(i) == p.charAt(j)) ++j;
            // pi[i]: 패턴의 0~i 구간에서 자신을 제외한 최장 공통 접두사·접미사 길이
            pi[i] = j;
        }

        // 본문 탐색과 겹치는 일치 처리
        j = 0;
        for (i = 0; i < n; ++i) {
            // 불일치 시 이미 일치한 부분의 접두사·접미사를 이용해 다음 후보 길이로 이동
            while (j > 0 && s.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (s.charAt(i) == p.charAt(j)) ++j;
            // 패턴 전체 일치: 시작 위치 기록 후 겹치는 다음 일치를 위해 j 복구
            if (j == m) {
                ans.add(i - m + 1);
                j = pi[j - 1];
            }
        }

        System.out.println(ans.size());
        for (int x : ans) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}
