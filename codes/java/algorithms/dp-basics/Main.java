import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        int[] dp;

        in = new Scanner(System.in);
        n = in.nextInt();
        dp = new int[21];

        // 피보나치 수열의 초기값
        dp[0] = 0;
        dp[1] = 1;
        for (i = 2; i <= n; ++i) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        System.out.println(dp[n]);
    }
}
