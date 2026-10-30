import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, q, i, j, x, a, b, c, d;
        int[][] p;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        q = in.nextInt();
        p = new int[n + 1][m + 1];
        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= m; ++j) {
                x = in.nextInt();
                p[i][j] = p[i - 1][j] + p[i][j - 1] - p[i - 1][j - 1] + x;
            }
        }
        for (i = 0; i < q; ++i) {
            a = in.nextInt();
            b = in.nextInt();
            c = in.nextInt();
            d = in.nextInt();
            System.out.println(p[c][d] - p[a - 1][d] - p[c][b - 1] + p[a - 1][b - 1]);
        }
    }
}
