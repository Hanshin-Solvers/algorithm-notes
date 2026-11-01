import java.util.Scanner;

public class Main {
    static int fact(int n) {
        if (n == 0) return 1;
        return n * fact(n - 1);
    }

    public static void main(String[] args) {
        Scanner in;
        int n;

        in = new Scanner(System.in);
        n = in.nextInt();
        System.out.println(fact(n));
    }
}
