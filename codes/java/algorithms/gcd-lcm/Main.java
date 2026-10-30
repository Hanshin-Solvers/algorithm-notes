import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int a, b, x, y, r;

        in = new Scanner(System.in);
        a = in.nextInt();
        b = in.nextInt();
        x = a;
        y = b;
        while (y != 0) {
            r = x % y;
            x = y;
            y = r;
        }

        System.out.println(x + " " + a / x * b);
    }
}
