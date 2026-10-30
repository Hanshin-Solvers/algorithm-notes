import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, r, i, p, f;

        in = new Scanner(System.in);
        n = in.nextInt();
        r = in.nextInt();
        p = 1;
        f = 1;
        for (i = 0; i < r; ++i) {
            p *= n - i;
            f *= i + 1;
        }

        System.out.println(p + " " + p / f);
    }
}
