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
                    // a의 i행과 b의 j열에서 같은 위치의 곱을 누적
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return c;
    }

    static int[][] power(int[][] a, int b) {
        int i;
        int[][] t;

        // 행렬의 0제곱은 대각 원소가 1인 항등행렬
        if (b == 0) {
            t = new int[n][n];
            for (i = 0; i < n; ++i) {
                t[i][i] = 1;
            }
            return t;
        }
        // 절반 지수의 결과를 한 번 계산하여 재사용
        t = power(a, b / 2);
        t = mul(t, t);
        // 홀수 지수에서 제곱 후 남은 행렬 a를 한 번 곱함
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
        // 절반 지수의 결과를 한 번 계산하여 재사용
        t = power(a, b);

        for (int[] row : t) {
            for (int x : row) {
                System.out.print(x + " ");
            }
            System.out.println();
        }
    }
}
