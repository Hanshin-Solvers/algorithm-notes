import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int n, i, j, cnt, pairs;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        cnt = 0;
        pairs = 0;

        // N번 실행
        for (i = 1; i <= n; ++i) {
            ++cnt;
        }

        // (N - 1) + (N - 2) + ... + 1번 실행
        for (i = 1; i <= n; ++i) {
            for (j = i + 1; j <= n; ++j) {
                ++pairs;
            }
        }

        System.out.println(cnt);
        System.out.println(pairs);
    }
}
