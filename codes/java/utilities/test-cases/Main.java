import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int t, n, i, j, x, sum;

        sc = new Scanner(System.in);
        t = sc.nextInt();
        for (i = 0; i < t; ++i) {
            n = sc.nextInt();
            // 케이스마다 합 초기화
            sum = 0;
            for (j = 0; j < n; ++j) {
                x = sc.nextInt();
                sum += x;
            }
            System.out.println(sum);
        }
    }
}
