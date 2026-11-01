import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, s, i, j, cnt;

        in = new Scanner(System.in);
        n = in.nextInt();
        s = in.nextInt();
        cnt = 0;

        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= n; ++j) {
                if (i + j == s) ++cnt;
            }
        }

        System.out.println(cnt);
    }
}
