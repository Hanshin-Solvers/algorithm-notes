import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, i, j;
        int[][] dp;
        String a, b;

        in = new Scanner(System.in);
        a = in.next();
        b = in.next();
        n = a.length();
        m = b.length();
        dp = new int[n + 1][m + 1];
        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= m; ++j) {
                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        System.out.println(dp[n][m]);
    }
}
