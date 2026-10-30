import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        boolean ok;

        in = new Scanner(System.in);
        n = in.nextInt();
        ok = n >= 2;
        for (i = 2; i <= n / i; ++i) {
            if (n % i == 0) ok = false;
        }

        System.out.println(ok ? "YES" : "NO");
    }
}
