import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int a, b, q, r, up;

        sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();

        q = Math.floorDiv(a, b);
        r = Math.floorMod(a, b);
        up = q;
        if (r > 0) ++up;

        System.out.println(q + " " + up + " " + r);
    }
}
