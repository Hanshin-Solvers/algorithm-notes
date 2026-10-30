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
            while (j > 0 && p.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (p.charAt(i) == p.charAt(j)) ++j;
            pi[i] = j;
        }

        // 본문 탐색과 겹치는 일치 처리
        j = 0;
        for (i = 0; i < n; ++i) {
            while (j > 0 && s.charAt(i) != p.charAt(j)) {
                j = pi[j - 1];
            }
            if (s.charAt(i) == p.charAt(j)) ++j;
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
