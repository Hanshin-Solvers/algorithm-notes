import java.util.*;

public class Main {
    static int power(int a, int b) {
        int x;

        if (b == 0) return 1;
        x = power(a, b / 2);
        x *= x;
        if (b % 2 == 1) x *= a;
        return x;
    }

    public static void main(String[] args) {
        Scanner in;
        int a, b;

        in = new Scanner(System.in);
        a = in.nextInt();
        b = in.nextInt();
        System.out.println(power(a, b));
    }
}
