import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, i, j;
        int[][] dp;
        String[] g;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        g = new String[n];
        dp = new int[n + 1][m + 1];
        for (i = 0; i < n; ++i) {
            g[i] = in.next();
        }
        // 시작 칸에 도착한 경우 한 가지로 초기화
        dp[1][1] = 1;
        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= m; ++j) {
                if (i == 1 && j == 1) continue;
                // 현재 칸으로 오는 위쪽 경로와 왼쪽 경로의 수를 합침
                if (g[i - 1].charAt(j - 1) == '1') dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        System.out.println(dp[n][m]);
    }
}
