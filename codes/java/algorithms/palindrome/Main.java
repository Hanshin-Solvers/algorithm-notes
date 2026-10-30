import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        String s;
        int l, r;
        boolean ok;

        sc = new Scanner(System.in);
        s = sc.next();
        l = 0;
        r = s.length() - 1;
        ok = true;

        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                ok = false;
                break;
            }
            ++l;
            --r;
        }

        System.out.println(ok ? "YES" : "NO");
    }
}
