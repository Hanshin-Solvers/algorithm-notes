import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, limit, i, c, w, v;
        int[] dp, un;

        in = new Scanner(System.in);
        n = in.nextInt();
        limit = in.nextInt();
        dp = new int[limit + 1];
        un = new int[limit + 1];
        for (i = 0; i < n; ++i) {
            w = in.nextInt();
            v = in.nextInt();
            // 큰 용량부터 갱신하여 같은 물건의 중복 선택 방지
            for (c = limit; c >= w; --c) {
                dp[c] = Math.max(dp[c], dp[c - w] + v);
            }
            // 작은 용량부터 갱신하여 같은 종류를 다시 선택
            for (c = w; c <= limit; ++c) {
                un[c] = Math.max(un[c], un[c - w] + v);
            }
        }
        System.out.println(dp[limit]);
        System.out.println(un[limit]);
    }
}
