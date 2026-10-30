import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        String s, p;
        int n, m, i, j;
        ArrayList<Integer> ans;

        sc = new Scanner(System.in);
        s = sc.next();
        p = sc.next();
        n = s.length();
        m = p.length();
        ans = new ArrayList<>();

        for (i = 0; i + m <= n; ++i) {
            j = 0;
            while (j < m && s.charAt(i + j) == p.charAt(j)) {
                ++j;
            }
            if (j == m) ans.add(i);
        }

        System.out.println(ans.size());
        for (int x : ans) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}
