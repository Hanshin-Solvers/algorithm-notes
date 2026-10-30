import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int b, c, x, d, i;
        String s, digit = "0123456789ABCDEF";
        StringBuilder out;

        in = new Scanner(System.in);
        b = in.nextInt();
        c = in.nextInt();
        s = in.next();
        x = 0;
        for (i = 0; i < s.length(); ++i) {
            d = digit.indexOf(s.charAt(i));
            x = x * b + d;
        }

        out = new StringBuilder();
        do {
            out.append(digit.charAt(x % c));
            x /= c;
        } while (x > 0);
        System.out.println(out.reverse());
    }
}
