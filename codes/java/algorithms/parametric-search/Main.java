import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, k, i, l, r, m, cnt, ans;
        int[] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        k = in.nextInt();
        a = new int[n];
        r = 0;
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
            r = Math.max(r, a[i]);
        }
        l = 1;
        ans = 0;
        while (l <= r) {
            m = (l + r) / 2;
            cnt = 0;
            for (int x : a) {
                cnt += x / m;
            }
            // 필요한 조각 수를 만들 수 있으면 답을 저장하고 더 긴 길이 탐색
            if (cnt >= k) {
                ans = m;
                l = m + 1;
            }
            // 조각 수가 부족하면 길이를 줄여 다시 탐색
            else r = m - 1;
        }
        System.out.println(ans);
    }
}
