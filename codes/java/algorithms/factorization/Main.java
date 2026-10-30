import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;

        in = new Scanner(System.in);
        n = in.nextInt();
        for (i = 2; i <= n / i; ++i) {
            while (n % i == 0) {
                System.out.print(i + " ");
                n /= i;
            }
        }
        if (n > 1) System.out.print(n);
        System.out.println();
    }
}
