import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        int[] dp;

        in = new Scanner(System.in);
        n = in.nextInt();
        dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (i = 2; i <= n; ++i) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        System.out.println(dp[n]);
    }
}
