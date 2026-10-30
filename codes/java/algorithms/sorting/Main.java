import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        int[][] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n][2];
        for (i = 0; i < n; ++i) {
            a[i][0] = in.nextInt();
            a[i][1] = in.nextInt();
        }
        // 점수 내림차순, 번호 오름차순
        Arrays.sort(a, (x, y) -> {
            if (x[1] != y[1]) return Integer.compare(y[1], x[1]);
            return Integer.compare(x[0], y[0]);
        });

        for (int[] x : a) {
            System.out.print(x[0] + " ");
        }
        System.out.println();
    }
}
