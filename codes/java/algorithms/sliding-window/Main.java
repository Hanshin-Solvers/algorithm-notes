import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, k, i, s, ans;
        int[] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        k = in.nextInt();
        a = new int[n];
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }
        s = 0;
        for (i = 0; i < k; ++i) {
            s += a[i];
        }
        ans = s;
        for (i = k; i < n; ++i) {
            s -= a[i - k];
            s += a[i];
            ans = Math.max(ans, s);
        }
        System.out.println(ans);
    }
}
