import java.util.*;

public class Main {
    public static void main(String[] args) {
        final boolean DEBUG = false;
        Scanner sc;
        int n, i, sum;
        int[] a;
        long start, finish;
        double ms;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new int[n];
        for (i = 0; i < n; ++i) {
            a[i] = sc.nextInt();
        }

        start = System.nanoTime();
        sum = 0;
        for (int x : a) {
            sum += x;
        }
        finish = System.nanoTime();
        ms = (finish - start) / 1000000.0;

        // DEBUG가 true이면 표준 오류에 기록
        if (DEBUG) {
            System.err.println("sum=" + sum);
            System.err.println("elapsed_ms=" + ms);
        }
        System.out.println(sum);
    }
}
