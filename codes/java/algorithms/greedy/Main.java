import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i, cnt, end;
        int[][] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n][2];
        for (i = 0; i < n; ++i) {
            a[i][0] = in.nextInt();
            a[i][1] = in.nextInt();
        }

        // 종료 시각 순서로 정렬
        Arrays.sort(a, Comparator.comparingInt(x -> x[1]));
        cnt = 0;
        end = 0;
        for (int[] x : a) {
            if (x[0] >= end) {
                ++cnt;
                end = x[1];
            }
        }

        System.out.println(cnt);
    }
}
