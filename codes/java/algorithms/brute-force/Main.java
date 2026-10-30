import java.util.*;

public class Main {
    static int n, target, cnt;

    static void search(int d, int s) {
        int x;

        if (d == 2) {
            if (s == target) ++cnt;
            return;
        }
        for (x = 1; x <= n; ++x) {
            search(d + 1, s + x);
        }
    }

    public static void main(String[] args) {
        Scanner in;

        in = new Scanner(System.in);
        n = in.nextInt();
        target = in.nextInt();
        search(0, 0);
        System.out.println(cnt);
    }
}
