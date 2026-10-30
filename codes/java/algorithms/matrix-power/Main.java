import java.util.*;

public class Main {
    static int n;

    static int[][] mul(int[][] a, int[][] b) {
        int i, j, k;
        int[][] c;

        c = new int[n][n];
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                for (k = 0; k < n; ++k) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return c;
    }

    static int[][] power(int[][] a, int b) {
        int i;
        int[][] t;

        if (b == 0) {
            t = new int[n][n];
            for (i = 0; i < n; ++i) {
                t[i][i] = 1;
            }
            return t;
        }
        t = power(a, b / 2);
        t = mul(t, t);
        if (b % 2 == 1) t = mul(t, a);
        return t;
    }

    public static void main(String[] args) {
        Scanner in;
        int b, i, j;
        int[][] a, t;

        in = new Scanner(System.in);
        n = in.nextInt();
        b = in.nextInt();
        a = new int[n][n];
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                a[i][j] = in.nextInt();
            }
        }
        t = power(a, b);

        for (int[] row : t) {
            for (int x : row) {
                System.out.print(x + " ");
            }
            System.out.println();
        }
    }
}
