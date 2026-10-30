import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, target, i, l, r, s, ans;
        int[] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        target = in.nextInt();
        a = new int[n];
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }
        l = 0;
        s = 0;
        ans = n + 1;
        for (r = 0; r < n; ++r) {
            s += a[r];
            while (s >= target) {
                ans = Math.min(ans, r - l + 1);
                s -= a[l];
                ++l;
            }
        }
        if (ans == n + 1) ans = 0;
        System.out.println(ans);
    }
}
