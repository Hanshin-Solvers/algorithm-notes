import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, q, i, x, l, r;
        int[] p;

        in = new Scanner(System.in);
        n = in.nextInt();
        q = in.nextInt();
        p = new int[n + 1];
        for (i = 1; i <= n; ++i) {
            x = in.nextInt();
            p[i] = p[i - 1] + x;
        }
        for (i = 0; i < q; ++i) {
            l = in.nextInt();
            r = in.nextInt();
            System.out.println(p[r] - p[l - 1]);
        }
    }
}
