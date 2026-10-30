import java.util.*;

public class Main {
    public static void main(String[] args) {
        final int INF = 1000000;
        Scanner sc;
        int n, m, i, j, k, a, b, w;
        int[][] d;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        d = new int[n + 1][n + 1];
        for (i = 1; i <= n; ++i) {
            Arrays.fill(d[i], INF);
            d[i][i] = 0;
        }
        for (i = 0; i < m; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            w = sc.nextInt();
            d[a][b] = Math.min(d[a][b], w);
        }

        for (k = 1; k <= n; ++k) {
            for (i = 1; i <= n; ++i) {
                for (j = 1; j <= n; ++j) {
                    if (d[i][k] == INF || d[k][j] == INF) continue;
                    d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }

        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= n; ++j) {
                if (d[i][j] == INF) System.out.print(-1 + " ");
                else System.out.print(d[i][j] + " ");
            }
            System.out.println();
        }
    }
}
