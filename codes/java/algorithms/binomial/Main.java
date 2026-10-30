import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, r, i, j;
        int[][] dp;

        in = new Scanner(System.in);
        n = in.nextInt();
        r = in.nextInt();
        dp = new int[n + 1][n + 1];
        for (i = 0; i <= n; ++i) {
            dp[i][0] = 1;
            dp[i][i] = 1;
            for (j = 1; j < i; ++j) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
        }
        System.out.println(dp[n][r]);
    }
}
