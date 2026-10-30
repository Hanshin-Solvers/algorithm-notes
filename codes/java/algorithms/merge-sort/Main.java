import java.util.*;

public class Main {
    static int[] a = new int[101], t = new int[101];

    static void sortRange(int l, int r) {
        int m, i, j, k;

        if (r - l <= 1) return;
        m = (l + r) / 2;
        sortRange(l, m);
        sortRange(m, r);

        i = l;
        j = m;
        k = l;
        while (i < m && j < r) {
            if (a[i] <= a[j]) {
                t[k] = a[i];
                ++i;
            }
            else {
                t[k] = a[j];
                ++j;
            }
            ++k;
        }
        while (i < m) {
            t[k] = a[i];
            ++k;
            ++i;
        }
        while (j < r) {
            t[k] = a[j];
            ++k;
            ++j;
        }
        for (i = l; i < r; ++i) {
            a[i] = t[i];
        }
    }

    public static void main(String[] args) {
        Scanner in;
        int n, i;

        in = new Scanner(System.in);
        n = in.nextInt();
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }
        sortRange(0, n);

        for (i = 0; i < n; ++i) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
}
