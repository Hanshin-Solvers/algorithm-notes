import java.util.*;

public class Main {
    static int cross(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]);
    }

    static boolean overlap(int a, int b, int c, int d) {
        return Math.max(Math.min(a, b), Math.min(c, d))
            <= Math.min(Math.max(a, b), Math.max(c, d));
    }

    public static void main(String[] args) {
        Scanner sc;
        int[] a, b, c, d;
        int x, y, z, w;
        boolean ok;

        sc = new Scanner(System.in);
        a = new int[]{sc.nextInt(), sc.nextInt()};
        b = new int[]{sc.nextInt(), sc.nextInt()};
        c = new int[]{sc.nextInt(), sc.nextInt()};
        d = new int[]{sc.nextInt(), sc.nextInt()};
        x = Integer.signum(cross(a, b, c));
        y = Integer.signum(cross(a, b, d));
        z = Integer.signum(cross(c, d, a));
        w = Integer.signum(cross(c, d, b));

        if (x == 0 && y == 0 && z == 0 && w == 0) {
            ok = overlap(a[0], b[0], c[0], d[0])
              && overlap(a[1], b[1], c[1], d[1]);
        }
        else ok = (x * y <= 0 && z * w <= 0);

        System.out.println(ok ? "YES" : "NO");
    }
}
