import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i, j;
        boolean[] prime;

        in = new Scanner(System.in);
        n = in.nextInt();
        prime = new boolean[n + 1];
        Arrays.fill(prime, true);
        prime[0] = false;
        prime[1] = false;
        for (i = 2; i * i <= n; ++i) {
            if (prime[i]) {
                for (j = i * i; j <= n; j += i) {
                    prime[j] = false;
                }
            }
        }

        for (i = 2; i <= n; ++i) {
            if (prime[i]) System.out.print(i + " ");
        }
        System.out.println();
    }
}
