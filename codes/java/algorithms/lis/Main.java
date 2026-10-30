import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i, x, l, r, m, len;
        int[] t;

        in = new Scanner(System.in);
        n = in.nextInt();
        t = new int[n];
        len = 0;
        for (i = 0; i < n; ++i) {
            x = in.nextInt();
            l = 0;
            r = len;
            while (l < r) {
                m = (l + r) / 2;
                if (t[m] < x) l = m + 1;
                else r = m;
            }
            t[l] = x;
            if (l == len) ++len;
        }
        System.out.println(len);
    }
}
