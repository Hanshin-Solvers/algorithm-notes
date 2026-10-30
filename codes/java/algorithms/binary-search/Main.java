import java.util.*;

public class Main {
    static int bound(int[] a, int x, boolean upper) {
        int l, r, m;

        l = 0;
        r = a.length;
        while (l < r) {
            m = (l + r) / 2;
            if (a[m] < x || (upper && a[m] == x)) l = m + 1;
            else r = m;
        }
        return l;
    }

    public static void main(String[] args) {
        Scanner in;
        int n, x, i;
        int[] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        x = in.nextInt();
        a = new int[n];
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }
        System.out.println(bound(a, x, true) - bound(a, x, false));
    }
}
