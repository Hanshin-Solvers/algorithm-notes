import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, q, i, l, r, x, s;
        int[] d;

        in = new Scanner(System.in);
        n = in.nextInt();
        q = in.nextInt();
        d = new int[n + 2];
        for (i = 0; i < q; ++i) {
            l = in.nextInt();
            r = in.nextInt();
            x = in.nextInt();
            d[l] += x;
            d[r + 1] -= x;
        }
        s = 0;
        for (i = 1; i <= n; ++i) {
            s += d[i];
            System.out.print(s + " ");
        }
        System.out.println();
    }
}
