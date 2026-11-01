import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, i, j;
        // dp[i][j]: 두 문자열의 앞 i개와 앞 j개 문자로 만든 LCS 길이
        int[][] dp;
        String a, b;
        StringBuilder ans;

        in = new Scanner(System.in);
        a = in.next();
        b = in.next();
        n = a.length();
        m = b.length();
        dp = new int[n + 1][m + 1];
        ans = new StringBuilder();

        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= m; ++j) {
                // 문자가 같으면 두 문자열에서 함께 선택
                if (a.charAt(i - 1) == b.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1] + 1;
                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }

        // 마지막 칸에서 문자를 선택하거나 길이가 유지되는 칸으로 이동
        i = n;
        j = m;
        while (i > 0 && j > 0) {
            // 문자가 같으면 두 문자열에서 함께 선택
            if (a.charAt(i - 1) == b.charAt(j - 1)) {
                ans.append(a.charAt(i - 1));
                --i;
                --j;
            }
            else if (dp[i - 1][j] >= dp[i][j - 1]) --i;
            else --j;
        }
        // 뒤에서부터 모은 문자를 뒤집어 원래 순서 복원
        ans.reverse();

        System.out.println(dp[n][m]);
        System.out.println(ans.toString());
    }
}
